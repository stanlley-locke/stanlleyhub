#!/bin/bash

# Define the root directory
ROOT_DIR="02-curriculum"

# Create the root and top-level files
mkdir -p "$ROOT_DIR"
touch "$ROOT_DIR/README.md" "$ROOT_DIR/curriculum-map.md" "$ROOT_DIR/course-structure.json"

# Create 00-shared and its files
mkdir -p "$ROOT_DIR/00-shared"
touch "$ROOT_DIR/00-shared/"{glossary.md,tools-and-workflow.md,github-workflow.md,project-management-core.md,capstone-guide.md,ai-safety-and-usage.md}

# Define the weekly folders in an array
weeks=(
    "01-orientation-project-management-git-github"
    "02-html-css-web-foundations"
    "03-javascript-fundamentals"
    "04-advanced-javascript-dom-debugging-collaboration"
    "05-react-fundamentals"
    "06-node-express-apis"
    "07-python-fundamentals-oop"
    "08-flask-django-basics"
    "09-databases-auth-architecture"
    "10-ai-ml-llms-agentic-ai"
    "11-linux-docker-deployment-devops"
    "12-capstone-demo-graduation"
)

# Loop through the array to create week folders and their standard files
for week in "${weeks[@]}"; do
    WEEK_PATH="$ROOT_DIR/weeks/$week"
    mkdir -p "$WEEK_PATH"
    touch "$WEEK_PATH/"{README.md,overview.md,tuesday.md,thursday.md,saturday.md,assignment.md,resources.md}
done

echo "Structure for $ROOT_DIR created successfully!"