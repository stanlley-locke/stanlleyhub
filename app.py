from flask import Flask, render_template, request, redirect, url_for, flash, session, abort
from werkzeug.security import generate_password_hash, check_password_hash
import os
from datetime import datetime, timedelta
import logging

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'stanleyhub-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stanleyhub.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=30)  # For "remember me" functionality

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Import and initialize db
from models import db
db.init_app(app)

# Import models after db initialization
from models import User, Course, Article, UserCourse, CourseStep, LearningMaterial

def create_sample_data():
    try:
        # --- Users ---
        admin = User(
            name='Admin User',
            email='admin@stanleyhub.com',
            password=generate_password_hash('Admin123'),
            is_admin=True
        )
        db.session.add(admin)

        user = User(
            name='Test User',
            email='user@example.com',
            password=generate_password_hash('Password123'),
            is_admin=False
        )
        db.session.add(user)

        # --- Courses ---
        courses_data = [
            {
                'title': 'Introduction to Cybersecurity',
                'description': 'Learn the fundamentals of cybersecurity including threat models, security principles, and basic security practices.',
                'image': 'cyber_intro.jpg',
                'category': 'cybersecurity',
                'level': 'beginner',
                'featured': True
            },
            {
                'title': 'Advanced Penetration Testing',
                'description': 'Master the art of ethical hacking with advanced penetration testing techniques and methodologies.',
                'image': 'pentest.jpg',
                'category': 'cybersecurity',
                'level': 'advanced',
                'featured': True
            },
            {
                'title': 'Full Stack Web Development',
                'description': 'Build complete web applications from front-end to back-end using modern frameworks and best practices.',
                'image': 'fullstack.jpg',
                'category': 'software_engineering',
                'level': 'intermediate',
                'featured': True
            },
            {
                'title': 'Python for Data Science',
                'description': 'Use Python to analyze and visualize data, build machine learning models, and extract insights.',
                'image': 'python_data.jpg',
                'category': 'software_engineering',
                'level': 'intermediate',
                'featured': False
            },
            {
                'title': 'Network Security Fundamentals',
                'description': 'Learn how to secure networks, implement firewalls, and protect against common network attacks.',
                'image': 'network_security.jpg',
                'category': 'cybersecurity',
                'level': 'beginner',
                'featured': False
            }
        ]

        # Create Course objects and keep references
        created_courses = {}
        for cd in courses_data:
            c = Course(
                title=cd['title'],
                description=cd['description'],
                image=cd.get('image'),
                category=cd.get('category'),
                level=cd.get('level'),
                featured=cd.get('featured', False)
            )
            db.session.add(c)
            # store by title for later reference
            created_courses[cd['title']] = c

        # Flush so course ids are assigned before creating dependent records
        db.session.flush()

        # --- Articles ---
        articles = [
            {
                'title': 'Understanding Zero Trust Security Model',
                'content': 'The Zero Trust security model assumes that threats exist both inside and outside traditional network boundaries. This article explores the principles of Zero Trust and how to implement it in your organization.',
                'category': 'cybersecurity',
                'image': 'zero_trust.jpg'
            },
            {
                'title': 'Best Practices for Secure Code Review',
                'content': 'Code reviews are essential for identifying security vulnerabilities before they make it to production. Learn the best practices for conducting effective security-focused code reviews.',
                'category': 'software_engineering',
                'image': 'code_review.jpg'
            },
            {
                'title': 'Introduction to OWASP Top 10',
                'content': 'The OWASP Top 10 is a standard awareness document for developers and web application security. It represents a broad consensus about the most critical security risks to web applications.',
                'category': 'cybersecurity',
                'image': 'owasp.jpg'
            },
            {
                'title': 'Containerization with Docker and Kubernetes',
                'content': 'Learn how to use Docker and Kubernetes to containerize and orchestrate your applications for better scalability and security.',
                'category': 'software_engineering',
                'image': 'containers.jpg'
            }
        ]

        for a in articles:
            article = Article(
                title=a['title'],
                content=a['content'],
                category=a.get('category'),
                image=a.get('image'),
                created_at=datetime.now()
            )
            db.session.add(article)

        db.session.flush()

        # --- Course Steps ---
        # Define steps per course title for clarity
        steps_by_course = {
            'Introduction to Cybersecurity': [
                ('Introduction', 'Welcome to the course!'),
                ('Getting Started', 'Learn the basics.')
            ],
            'Advanced Penetration Testing': [
                ('Advanced Topics', 'Dive deeper into penetration testing.'),
                ('Ethical Hacking Practices', 'Ethics and legality of hacking.')
            ],
            'Full Stack Web Development': [
                ('Frontend Development', 'Learn about HTML, CSS, and JavaScript.'),
                ('Backend Development', 'Learn about server-side programming.')
            ],
            'Python for Data Science': [
                ('Data Analysis', 'Learn how to analyze data using Python.'),
                ('Machine Learning', 'Intro to machine learning.')
            ],
            'Network Security Fundamentals': [
                ('Network Basics', 'Understand the basics of computer networks.'),
                ('Firewall Configuration', 'Learn how to configure firewalls.')
            ]
        }

        # Create CourseStep rows
        for course_title, steps in steps_by_course.items():
            course_obj = created_courses.get(course_title)
            if not course_obj:
                continue
            for idx, (step_title, step_desc) in enumerate(steps, start=1):
                step = CourseStep(
                    course_id=course_obj.id,
                    title=step_title,
                    description=step_desc,
                    number=idx
                )
                db.session.add(step)

        db.session.flush()

        # --- Learning Materials ---
        # Provide explicit titles — fallback to generated title if missing
        learning_materials = []
        for course_title, steps in steps_by_course.items():
            course_obj = created_courses.get(course_title)
            if not course_obj:
                continue
            for idx, (step_title, step_desc) in enumerate(steps, start=1):
                lm = {
                    'course_id': course_obj.id,
                    'step_number': idx,
                    'material_type': 'text',
                    'title': f'{step_title} - Overview',
                    'content': f'{step_title}: {step_desc}'
                }
                learning_materials.append(lm)

        # Add to DB
        for m in learning_materials:
            title = m.get('title') or f"Step {m['step_number']} - Material"
            material = LearningMaterial(
                course_id=m['course_id'],
                step_number=m['step_number'],
                material_type=m['material_type'],
                title=title,
                url=m.get('url'),
                content=m.get('content')
            )
            db.session.add(material)

        # Final commit
        db.session.commit()
        print("Sample data created successfully!")

    except Exception as e:
        db.session.rollback()
        logging.exception("Error creating sample data")
        print(f"Error creating sample data: {str(e)}")
        raise


def init_db():
    try:
        # Create all tables
        db.create_all()

        # Add initial data if database is empty
        if not User.query.first():
            create_sample_data()

    except Exception as e:
        print(f"Database initialization error: {str(e)}")
        raise

# Utility function to get current user
def get_current_user():
    if 'user_id' in session:
        return User.query.get(session['user_id'])
    return None

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# Context processor to make current_user available in all templates
@app.context_processor
def inject_user():
    return dict(current_user=get_current_user())

# Routes for authentication
@app.route('/')
def index():
    try:
        featured_courses = Course.query.filter_by(featured=True).limit(3).all()
        recent_articles = Article.query.order_by(Article.created_at.desc()).limit(4).all()
        return render_template('index.html', featured_courses=featured_courses, recent_articles=recent_articles)
    except Exception as e:
        flash(f"An error occurred: {str(e)}")
        return render_template('index.html', featured_courses=[], recent_articles=[])

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False

        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            flash('Please check your login details and try again.')
            return redirect(url_for('login'))

        session['user_id'] = user.id
        if remember:
            session.permanent = True

        flash('Login successful!')
        return redirect(url_for('dashboard'))

    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm-password')

        if not name or not email or not password or not confirm_password:
            flash('All fields are required.')
            return redirect(url_for('signup'))

        if password != confirm_password:
            flash('Passwords do not match.')
            return redirect(url_for('signup'))

        if len(password) < 8:
            flash('Password must be at least 8 characters long.')
            return redirect(url_for('signup'))

        if User.query.filter_by(email=email).first():
            flash('Email address already exists.')
            return redirect(url_for('signup'))

        try:
            new_user = User(
                name=name,
                email=email,
                password=generate_password_hash(password)
            )
            db.session.add(new_user)
            db.session.commit()

            flash('Account created successfully! Please log in.')
            return redirect(url_for('login'))
        except Exception as e:
            db.session.rollback()
            flash(f'An error occurred: {str(e)}')
            return redirect(url_for('signup'))

    return render_template('signup.html')

@app.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form.get('email')
        if not email:
            flash('Email is required.')
            return redirect(url_for('forgot_password'))

        if not User.query.filter_by(email=email).first():
            flash('No account found with that email address.')
            return redirect(url_for('forgot_password'))

        flash('Password reset link has been sent to your email.')
        return redirect(url_for('login'))

    return render_template('forgot_password.html')

@app.route('/reset-password', methods=['GET', 'POST'])
def reset_password():
    if request.method == 'POST':
        new_password = request.form.get('new-password')
        confirm_new_password = request.form.get('confirm-new-password')

        if not new_password or not confirm_new_password:
            flash('All fields are required.')
            return redirect(url_for('reset_password'))

        if new_password != confirm_new_password:
            flash('Passwords do not match.')
            return redirect(url_for('reset_password'))

        if len(new_password) < 8:
            flash('Password must be at least 8 characters long.')
            return redirect(url_for('reset_password'))

        flash('Password has been reset successfully. Please log in with your new password.')
        return redirect(url_for('login'))

    return render_template('reset_password.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out.')
    return redirect(url_for('index'))

# Protected routes
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('Please log in to access your dashboard.')
        return redirect(url_for('login'))

    try:
        user = User.query.get_or_404(session['user_id'])
        user_courses = UserCourse.query.filter_by(user_id=user.id).all()
        enrolled_courses = [uc.course for uc in user_courses]

        recommended_courses = Course.query.filter(
            ~Course.id.in_([c.id for c in enrolled_courses])
        ).limit(2).all()

        return render_template(
            'dashboard.html',
            user=user,
            enrolled_courses=enrolled_courses,
            recommended_courses=recommended_courses
        )
    except Exception as e:
        flash(f'An error occurred: {str(e)}')
        return redirect(url_for('index'))

@app.route('/courses')
def courses():
    try:
        category = request.args.get('category', 'all')
        level = request.args.get('level', 'all')
        query = Course.query

        if category != 'all':
            query = query.filter_by(category=category)
        if level != 'all':
            query = query.filter_by(level=level)

        all_courses = query.all()
        categories = [c[0] for c in db.session.query(Course.category).distinct().all()]
        levels = [l[0] for l in db.session.query(Course.level).distinct().all()]

        return render_template(
            'courses.html',
            courses=all_courses,
            categories=categories,
            levels=levels,
            selected_category=category,
            selected_level=level
        )
    except Exception as e:
        flash(f'An error occurred: {str(e)}')
        return render_template('courses.html', courses=[])

@app.route('/course/<int:course_id>')
def course_detail(course_id):
    try:
        course = Course.query.get_or_404(course_id)
        is_enrolled = False

        if 'user_id' in session:
            is_enrolled = UserCourse.query.filter_by(
                user_id=session['user_id'],
                course_id=course_id
            ).first() is not None

        related_courses = Course.query.filter_by(
            category=course.category
        ).filter(Course.id != course.id).limit(3).all()

        return render_template(
            'course_detail.html',
            course=course,
            is_enrolled=is_enrolled,
            related_courses=related_courses
        )
    except Exception as e:
        flash(f'An error occurred: {str(e)}')
        return redirect(url_for('courses'))

@app.route('/enroll/<int:course_id>')
def enroll(course_id):
    if 'user_id' not in session:
        flash('Please log in to enroll in courses.')
        return redirect(url_for('login'))

    try:
        course = Course.query.get_or_404(course_id)
        existing = UserCourse.query.filter_by(
            user_id=session['user_id'],
            course_id=course_id
        ).first()
        if existing:
            flash('You are already enrolled in this course.')
            return redirect(url_for('course_detail', course_id=course_id))

        db.session.add(UserCourse(user_id=session['user_id'], course_id=course_id))
        db.session.commit()

        flash(f'Successfully enrolled in {course.title}!')
        return redirect(url_for('dashboard'))
    except Exception as e:
        db.session.rollback()
        flash(f'An error occurred: {str(e)}')
        return redirect(url_for('course_detail', course_id=course_id))

@app.route('/articles')
def articles():
    try:
        category = request.args.get('category', 'all')
        query = Article.query.order_by(Article.created_at.desc())
        if category != 'all':
            query = query.filter_by(category=category)

        all_articles = query.all()
        categories = [c[0] for c in db.session.query(Article.category).distinct().all()]

        return render_template(
            'articles.html',
            articles=all_articles,
            categories=categories,
            selected_category=category
        )
    except Exception as e:
        flash(f'An error occurred: {str(e)}')
        return render_template('articles.html', articles=[])

@app.route('/article/<int:article_id>')
def article_detail(article_id):
    try:
        article = Article.query.get_or_404(article_id)
        related_articles = Article.query.filter_by(
            category=article.category
        ).filter(Article.id != article.id).limit(2).all()
        popular_courses = Course.query.filter_by(featured=True).limit(2).all()

        return render_template(
            'article_detail.html',
            article=article,
            related_articles=related_articles,
            popular_courses=popular_courses
        )
    except Exception as e:
        flash(f'An error occurred: {str(e)}')
        return redirect(url_for('articles'))

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'user_id' not in session:
        flash('Please log in to access your profile.')
        return redirect(url_for('login'))

    try:
        user = User.query.get_or_404(session['user_id'])

        if request.method == 'POST':
            name = request.form.get('name')
            current_password = request.form.get('current_password')
            new_password = request.form.get('new_password')
            confirm_password = request.form.get('confirm_password')

            if name and name != user.name:
                user.name = name

            if current_password and new_password and confirm_password:
                if not check_password_hash(user.password, current_password):
                    flash('Current password is incorrect.')
                    return redirect(url_for('profile'))

                if new_password != confirm_password:
                    flash('New passwords do not match.')
                    return redirect(url_for('profile'))

                if len(new_password) < 8:
                    flash('New password must be at least 8 characters long.')
                    return redirect(url_for('profile'))

                user.password = generate_password_hash(new_password)

            db.session.commit()
            flash('Profile updated successfully!')
            return redirect(url_for('profile'))

        return render_template('profile.html', user=user)
    except Exception as e:
        flash(f'An error occurred: {str(e)}')
        return redirect(url_for('dashboard'))

@app.route('/search')
def search():
    try:
        query_str = request.args.get('q', '')
        if not query_str:
            return render_template('search.html', results={'courses': [], 'articles': []}, query='')

        courses = Course.query.filter(
            (Course.title.ilike(f'%{query_str}%')) |
            (Course.description.ilike(f'%{query_str}%'))
        ).all()
        articles = Article.query.filter(
            (Article.title.ilike(f'%{query_str}%')) |
            (Article.content.ilike(f'%{query_str}%'))
        ).all()

        return render_template('search.html', results={'courses': courses, 'articles': articles}, query=query_str)
    except Exception as e:
        flash(f'An error occurred: {str(e)}')
        return render_template('search.html', results={'courses': [], 'articles': []}, query='')

@app.route('/create_error_templates')
def create_error_templates():
    os.makedirs('templates', exist_ok=True)

    if not os.path.exists('templates/404.html'):
        with open('templates/404.html', 'w') as f:
            f.write('''
{% extends 'base.html' %}

{% block title %}Page Not Found | StanleyHub{% endblock %}

{% block content %}
<div class="error-container">
    <div class="error-content">
        <h1>404</h1>
        <h2>Page Not Found</h2>
        <p>The page you are looking for does not exist or has been moved.</p>
        <a href="{{ url_for('index') }}" class="btn-primary">Go to Homepage</a>
    </div>
</div>
{% endblock %}
''')

    if not os.path.exists('templates/500.html'):
        with open('templates/500.html', 'w') as f:
            f.write('''
{% extends 'base.html' %}

{% block title %}Server Error | StanleyHub{% endblock %}

{% block content %}
<div class="error-container">
    <div class="error-content">
        <h1>500</h1>
        <h2>Server Error</h2>
        <p>Something went wrong on our end. Please try again later.</p>
        <a href="{{ url_for('index') }}" class="btn-primary">Go to Homepage</a>
    </div>
</div>
{% endblock %}
''')

    return "Error templates created!"

@app.route('/learning/<int:course_id>', methods=['GET'])
def learning(course_id):
    step = request.args.get('step', default=1, type=int)
    course = Course.query.get_or_404(course_id)

    # Fetch steps dynamically from the database
    steps = CourseStep.query.filter_by(course_id=course_id).order_by(CourseStep.number).all()
    current_step = next((s for s in steps if s.number == step), None)
    previous_step = next((s for s in steps if s.number == step - 1), None)
    next_step = next((s for s in steps if s.number == step + 1), None)

    # Fetch learning materials for the current step
    materials = LearningMaterial.query.filter_by(course_id=course_id, step_number=step).all()

    # Log fetched data for debugging
    logging.debug(f"Course: {course}")
    logging.debug(f"Steps: {steps}")
    logging.debug(f"Current Step: {current_step}")
    logging.debug(f"Materials: {materials}")

    progress = (step / len(steps)) * 100 if steps else 0

    return render_template('learning.html', course=course, steps=steps, current_step=current_step, previous_step=previous_step, next_step=next_step, progress=progress, materials=materials)

if __name__ == '__main__':
    with app.app_context():
        # Initialize database (tables + sample data)
        init_db()

        # Ensure error templates are present
        create_error_templates()

    # Start the Flask development server
    app.run(host='0.0.0.0', port=8080, debug=True)
