# 🚀 The Algorithm™ Growth Velocity System

> **"We don't measure where you are. We measure how fast you're improving."**

A GitHub-native gamification system that rewards learning velocity over absolute skill. Perfect for educational environments where AI assistance is mandatory and growth mindset is the goal.

![Growth Tracker](../../actions/workflows/growth-tracker.yml/badge.svg)
[![Learning Velocity](https://img.shields.io/badge/Learning%20Velocity-Accelerating-brightgreen)](METRICS.md)

## ✨ What Makes This Different

- **📈 Measures dy/dx, not y** - Your rate of improvement matters, not your current skill
- **🤖 AI-Positive** - Rewards iterating on AI output, not just using it
- **🎯 Growth Mindset** - Failing 3 times then succeeding = more points than perfection
- **💬 Instant Feedback** - Every PR gets personalized growth coaching
- **📊 Public Metrics** - Transparent leaderboard updates every 6 hours

## 🚀 30-Second Setup

```bash
# Run this in any GitHub repository:
curl -sSL https://raw.githubusercontent.com/algocratic/growth-tracker/main/setup.sh | bash

# Or download and run:
wget https://raw.githubusercontent.com/algocratic/growth-tracker/main/setup.sh
chmod +x setup.sh
./setup.sh
```

That's it! The system is now active. Push to GitHub and watch the magic happen.

## 📊 How Scoring Works

### Base Points
- **Commit**: +5 pts
- **Pull Request**: +20 pts
- **Issue Closed**: +25 pts

### Growth Multipliers
- **Iterations** (`v2`, `attempt 3`): +15 pts each
- **Tests Added**: +20 pts
- **Refactoring**: +20 pts
- **AI Improvement** (modified AI output): +25 pts
- **Collaboration** (pairing, reviews): +20 pts

### The Growth Formula
```
Weekly Velocity = This Week's Score - Last Week's Score
Growth Trajectory = Current Velocity - Previous Velocity
```

## 🎮 Example Scenarios

### Scenario 1: The Perfectionist (Low Growth)
```bash
git commit -m "implemented feature perfectly on first try"
# Score: 5 points
# Velocity: 0 (no growth demonstrated)
```

### Scenario 2: The Learner (High Growth)
```bash
git commit -m "feat: initial attempt at auth system"
git commit -m "fix: iteration 2 - fixed token validation"
git commit -m "test: added edge cases discovered during debugging"
git commit -m "refactor: improved based on PR feedback from @teammate"
# Score: 65 points
# Velocity: +65 (massive growth!)
```

## 📈 What You Get

### 1. Automatic PR Comments
Every pull request receives personalized feedback:
```markdown
## 🚀 ACCELERATING Growth Report

Hey @developer! Your velocity of +45 pts/week is crushing it!

What's Working:
- Excellent iteration habits (5 refinements)
- Mature AI collaboration (not just copy-paste)
- Strong team player (helped 3 others)

Next Level: Try that scary refactor you've been avoiding!
```

### 2. Public Leaderboard (METRICS.md)
```markdown
| Rank | Developer | Velocity | Trajectory | Status |
|------|-----------|----------|------------|--------|
| 🥇 | @learner | +87/week | 🚀 ACCELERATING | Crushing It! |
| 🥈 | @improver | +45/week | 📈 IMPROVING | Solid Growth |
| 🥉 | @steady | +12/week | ➡️ STEADY | Keep Pushing |
```

### 3. Growth Insights
- Track AI tool effectiveness
- Identify learning patterns
- Celebrate iteration over perfection
- Reward helping others

## 🎯 For Instructors

### Why This Works
1. **Safe Failure** - "Iteration 3" sounds better than "failed twice"
2. **Visible Progress** - Public metrics create positive peer pressure
3. **AI Integration** - Teaches how to improve AI output, not just use it
4. **Growth Focus** - Beginners can outscore experts by learning faster

### Customization Options
- Adjust point values in `.github/workflows/growth-tracker.yml`
- Add custom challenges in `METRICS.md`
- Create team competitions
- Set weekly growth targets

### Metrics That Matter
```yaml
What We Track:
  - Iteration attempts (growth mindset)
  - AI modification rate (critical thinking)
  - Help given/received (collaboration)
  - Test coverage added (quality focus)
  - Refactoring frequency (code craft)

What We Ignore:
  - Lines of code (meaningless)
  - Commit count alone (quality > quantity)
  - Current skill level (starting point doesn't matter)
```

## 🤝 For Students

### How to Maximize Your Score

1. **Iterate Publicly**
   ```bash
   git commit -m "attempt 1: basic implementation"
   git commit -m "attempt 2: fixed edge case"
   git commit -m "attempt 3: working solution!"
   ```

2. **Improve AI Output**
   ```bash
   git commit -m "initial: GitHub Copilot suggestion"
   git commit -m "enhanced: added error handling AI missed"
   git commit -m "refined: made code more readable"
   ```

3. **Collaborate Often**
   ```bash
   git commit -m "paired with @teammate on auth logic"
   git commit -m "incorporated @reviewer's feedback"
   ```

4. **Test Everything**
   ```bash
   git commit -m "test: added unit tests for new feature"
   git commit -m "test: edge cases based on PR discussion"
   ```

## 🏆 Achievements & Badges

The system automatically recognizes:
- 🚀 **Velocity Champion** - Highest weekly growth
- 🤖 **AI Whispere