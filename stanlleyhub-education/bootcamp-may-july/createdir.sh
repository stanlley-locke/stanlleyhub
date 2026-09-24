#!/bin/bash

echo "Populating subfolders and files within the current directory..."

# 1. Create shared and weeks directories inside existing folders
mkdir -p "03-assignments/00-shared"
mkdir -p "03-assignments/weeks"
mkdir -p "04-slides/00-shared"
mkdir -p "04-slides/weeks"
mkdir -p "05-recordings/00-shared"
mkdir -p "05-recordings/weeks"

# 2. Populate base and shared files for 03-assignments
touch "03-assignments/"{README.md,assignments-map.md,submission-guide.md,grading-overview.md}
touch "03-assignments/00-shared/"{README.md,github-submission-rules.md,naming-conventions.md,project-board-rules.md,assignment-checklist.md,reflection-template.md,peer-review-template.md,capstone-submission-requirements.md}

# 3. Populate base and shared files for 04-slides
touch "04-slides/"{README.md,slides-map.md,slide-style-guide.md}
touch "04-slides/00-shared/"{README.md,bootcamp-cover-slide.md,standard-slide-outline.md,lesson-opening-template.md,assignment-slide-template.md,checkpoint-slide-template.md,demo-day-slide-template.md,visual-asset-notes.md}

# 4. Populate base and shared files for 05-recordings
touch "05-recordings/"{README.md,recordings-map.md,naming-convention.md,upload-workflow.md}
touch "05-recordings/00-shared/"{README.md,recording-checklist.md,post-class-processing-guide.md,recap-template.md,missing-class-guide.md,recording-metadata-template.md}

# 5. Define weeks array (Folder Name | Assignment Number | Specific Starter Pack File)
weeks=(
  "01-orientation-project-management-git-github|01|sample-project-scope-template.md"
  "02-html-css-web-foundations|02|portfolio-structure-template.md"
  "03-javascript-fundamentals|03|js-mini-project-ideas.md"
  "04-advanced-javascript-dom-debugging-collaboration|04|pair-project-workflow.md"
  "05-react-fundamentals|05|react-project-ideas.md"
  "06-node-express-apis|06|api-endpoint-template.md"
  "07-python-fundamentals-oop|07|python-cli-ideas.md"
  "08-flask-django-basics|08|framework-project-options.md"
  "09-databases-auth-architecture|09|schema-template.md"
  "10-ai-ml-llms-agentic-ai|10|ai-workflow-template.md"
  "11-linux-docker-deployment-devops|11|deployment-checklist-template.md"
  "12-capstone-demo-graduation|12|custom" # Week 12 is handled conditionally
)

# 6. Generate the week-by-week structure
for entry in "${weeks[@]}"; do
  IFS='|' read -r wname num starter <<< "$entry"

  # --- 03-assignments week folders ---
  aw="03-assignments/weeks/$wname"
  mkdir -p "$aw/starter-pack"
  touch "$aw/"{README.md,assignment-${num}-overview.md,assignment-${num}-main.md,rubric.md,submission.md,examples.md}
  touch "$aw/starter-pack/README.md"
  
  if [ "$num" == "12" ]; then
    touch "$aw/starter-pack/capstone-brief-template.md"
    touch "$aw/starter-pack/capstone-demo-template.md"
  else
    touch "$aw/starter-pack/$starter"
  fi

  # --- 04-slides week folders ---
  sw="04-slides/weeks/$wname"
  mkdir -p "$sw"
  touch "$sw/"{README.md,tuesday-slides.md,thursday-slides.md,saturday-slides.md,speaker-notes.md}

  # --- 05-recordings week folders ---
  rw="05-recordings/weeks/$wname"
  mkdir -p "$rw/"{tuesday,thursday,saturday}
  touch "$rw/README.md"

  # Populate detailed daily recording files explicitly for weeks 01 and 12 (as per the provided tree)
  if [ "$num" == "01" ] || [ "$num" == "12" ]; then
    for day in tuesday thursday saturday; do
      touch "$rw/$day/"{recording-link.md,recap.md,timestamps.md,attachments.md}
    done
  fi
done

echo "Success! The internal structure has been populated."