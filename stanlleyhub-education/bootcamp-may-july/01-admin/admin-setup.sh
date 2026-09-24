#!/bin/bash

# Ensure we are creating these inside the 01-admin folder
echo "Creating admin folder structure..."

# 00-overview
mkdir -p 00-overview
touch 00-overview/{README.md,bootcamp-summary.md,bootcamp-roadmap.md,weekly-structure.md,admin-checklist.md}

# 01-policies
mkdir -p 01-policies
touch 01-policies/{attendance-policy.md,assignment-policy.md,certificate-policy.md,communication-policy.md,code-of-conduct.md,ai-usage-policy.md,late-submission-policy.md,project-collaboration-policy.md}

# 02-onboarding
mkdir -p 02-onboarding
touch 02-onboarding/{onboarding-checklist.md,onboarding-form-questions.md,student-welcome-message.md,onboarding-orientation-plan.md,pre-bootcamp-setup-guide.md,tools-installation-guide.md,student-introduction-template.md,accepted-student-next-steps.md}

# 03-schedules
mkdir -p 03-schedules
touch 03-schedules/{master-calendar.md,class-timetable.md,weekly-release-schedule.md,important-dates.md,demo-day-run-sheet.md}

# 04-instructor-guides
mkdir -p 04-instructor-guides
touch 04-instructor-guides/{teaching-guidelines.md,class-delivery-framework.md,live-session-checklist.md,saturday-review-format.md,code-review-guidelines.md,project-review-guidelines.md,pair-programming-guidelines.md,struggling-student-support-playbook.md}

# 05-lesson-plans
mkdir -p 05-lesson-plans
touch 05-lesson-plans/week-{01..12}-lesson-plan.md

# 06-templates
mkdir -p 06-templates
touch 06-templates/{class-recap-template.md,weekly-roadmap-template.md,assignment-template.md,project-brief-template.md,README-template.md,sprint-planning-template.md,retrospective-template.md,code-review-template.md,attendance-sheet-template.csv,grading-sheet-template.csv,certificate-template-text.md,feedback-form-template.md}

# 07-communication
mkdir -p 07-communication/whatsapp-announcements 07-communication/classroom-posts 07-communication/private-messages
touch 07-communication/whatsapp-announcements/{welcome-message.md,weekly-roadmap-post.md,class-reminder-post.md,assignment-reminder-post.md,blocker-checkin-post.md,saturday-demo-prompt.md,graduation-message.md}
touch 07-communication/classroom-posts/{module-release-post.md,assignment-post-template.md,class-recap-post-template.md,submission-instructions-template.md}
touch 07-communication/private-messages/{absent-student-followup.md,struggling-student-checkin.md,late-submission-followup.md,certificate-eligibility-message.md}

# 08-tracking
mkdir -p 08-tracking/{attendance,assignments,participation,capstone,certification}
touch 08-tracking/attendance/{attendance-master.csv,weekly-attendance-log.md}
touch 08-tracking/assignments/{assignment-tracker.csv,submission-status-log.md}
touch 08-tracking/participation/{participation-tracker.csv,engagement-log.md}
touch 08-tracking/capstone/{capstone-progress-tracker.csv,capstone-review-log.md}
touch 08-tracking/certification/{certificate-eligibility-tracker.csv,completion-status-log.md}

# 09-assessment
mkdir -p 09-assessment
touch 09-assessment/{grading-rubric-overview.md,weekly-assignment-rubric.md,project-rubric.md,capstone-rubric.md,demo-day-rubric.md,participation-rubric.md}

# 10-certificates
mkdir -p 10-certificates
touch 10-certificates/{certificate-criteria.md,certificate-issuance-process.md,certificate-signoff-list.md,award-categories.md}

# 11-project-management
mkdir -p 11-project-management
touch 11-project-management/{pm-framework.md,sprint-cycle-guide.md,backlog-management-guide.md,kanban-board-guide.md,standup-format.md,retrospective-format.md,capstone-project-flow.md}

# 12-support
mkdir -p 12-support
touch 12-support/{faq.md,troubleshooting-guide.md,github-common-issues.md,setup-common-issues.md,classroom-common-issues.md,meet-session-common-issues.md}

# 13-post-bootcamp
mkdir -p 13-post-bootcamp
touch 13-post-bootcamp/{offboarding-checklist.md,testimonial-request-template.md,feedback-survey-plan.md,alumni-group-plan.md,graduation-runbook.md,next-cohort-improvement-notes.md}

echo "All folders and files created successfully in 01-admin!"
ls -R