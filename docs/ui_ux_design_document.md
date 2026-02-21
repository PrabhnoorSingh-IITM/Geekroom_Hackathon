# InsightForge - UI/UX Design Document

## 1. Design Philosophy

The V3 redesign of InsightForge prioritizes a **Google-Style Minimalist Search Interface**. Instead of overwhelming non-technical users with complex data upload panels, the interface is stripped down to an elegant, centralized search bar.

## 2. Core Aesthetics

- **Color Palette & Theme:** Employs a deep dark mode featuring Cyber-Blue (`#00d4ff`) and Emerald (`#00ff88`) gradients to convey high-tech, enterprise AI capabilities.
- **Glassmorphism:** Navigation menus, floating action bars, and analytical cards utilize `backdrop-filter: blur(24px)` to achieve transparency without sacrificing content readability against the animated orb background.
- **Micro-Animations:** Hovering over search bars, CTA buttons, and output reports triggers a cohesive `transform: translateY(-2px)` lift paired with expanded `box-shadow` glows to provide robust tactile feedback.

## 3. Interaction Design

- **The Story Arc:** The journey spans from problem-identification on the Landing page, direct problem resolution natively tracked inside the Dashboard search, and deep transparency provided in the 'The Story' organizational page.
- **Graceful Loading:** Uses a pulsating CSS loader (`.loader`) and sequential DOM reveal animations when rendering the final AI analytics to build anticipation and emulate active programmatic "thinking".
