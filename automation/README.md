# LegalDecode Automation — Starter

This directory is an isolated automation foundation on the `automation-setup` branch.

## Safety rules
- This workflow is manual-only (`workflow_dispatch`). It does not run on a schedule.
- It does not modify the website files or the `main` branch.
- It does not publish to YouTube, Instagram, Facebook, or any other service.
- It does not require API keys or paid services for this starter run.
- A package must remain **READY FOR REVIEW** until the user explicitly approves that specific package with **DONE**.

## Current capability
The starter workflow creates a review-package template and checks that mandatory legal-verification and approval fields are present. It does not yet perform legal research, render MP4 videos, or upload/schedule posts.

## Next integrations (not configured)
1. Authentic legal-source retrieval and citation verification.
2. Hindi/English script and slide generation in LegalDecode style.
3. Video rendering and subtitle/voiceover generation.
4. Private review delivery.
5. Publishing integrations, only after explicit per-package DONE approval.

Do not add credentials to source files. Use GitHub Actions Secrets only after the exact service, permissions, and cost implications have been reviewed with the user.
