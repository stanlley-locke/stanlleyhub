from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Create db instance without initializing it
db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return f'<User {self.email}>'

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(100), nullable=True)
    category = db.Column(db.String(50), nullable=False)
    level = db.Column(db.String(20), nullable=False)
    featured = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return f'<Course {self.title}>'

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(100), nullable=True)
    category = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return f'<Article {self.title}>'

class UserCourse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    enrolled_at = db.Column(db.DateTime, default=datetime.now)

    user = db.relationship('User', backref=db.backref('courses', lazy=True))
    course = db.relationship('Course', backref=db.backref('users', lazy=True))

    def __repr__(self):
        return f'<UserCourse {self.user_id}:{self.course_id}>'

class CourseStep(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    video_url = db.Column(db.String(200), nullable=True)

    course = db.relationship('Course', backref=db.backref('steps', lazy=True))

    def __repr__(self):
        return f'<CourseStep {self.course_id}:{self.number}>'

class UserProgress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    step_number = db.Column(db.Integer, nullable=False)

    user = db.relationship('User', backref=db.backref('progress', lazy=True))
    course = db.relationship('Course', backref=db.backref('progress', lazy=True))

    def __repr__(self):
        return f'<UserProgress {self.user_id}:{self.course_id}:{self.step_number}>'

class LearningMaterial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    step_number = db.Column(db.Integer, nullable=False)
    material_type = db.Column(db.String(50), nullable=False)  # e.g., 'video', 'document', 'quiz'
    title = db.Column(db.String(200), nullable=False)
    url = db.Column(db.String(500), nullable=True)  # For external links
    content = db.Column(db.Text, nullable=True)  # For embedded content like quizzes

    course = db.relationship('Course', backref=db.backref('materials', lazy=True))

    def __repr__(self):
        return f'<LearningMaterial {self.course_id}:{self.step_number}:{self.material_type}>'