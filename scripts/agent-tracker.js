#!/usr/bin/env node

/**
 * Agent Contribution Tracker
 * Tracks and displays which agents contributed to a given PR
 */

const fs = require('fs').promises;
const path = require('path');
const { execSync } = require('child_process');

// Agent registry with their roles and emojis
const AGENTS = {
  'product-architect-advisor': {
    name: 'Product Architect Advisor',
    emoji: '🏛️',
    role: 'System Architecture & Strategic Decisions'
  },
  'scrum-architect-owner': {
    name: 'Scrum Architect-Owner',
    emoji: '🎯',
    role: 'Product Ownership & Technical Architecture'
  },
  'scrum-project-manager': {
    name: 'Scrum Project Manager',
    emoji: '📋',
    role: 'Sprint Planning & GitHub Workflow'
  },
  'scrum-team-engineer': {
    name: 'Scrum Team Engineer',
    emoji: '⚙️',
    role: 'Code Implementation & Reviews'
  },
  'test-engineer': {
    name: 'Test Engineer',
    emoji: '🧪',
    role: 'Testing Strategy & Quality Assurance'
  },
  'kevin-github-algorithm': {
    name: 'Kevin (GitHub Algorithm)',
    emoji: '🔍',
    role: 'GitHub Process Compliance'
  },
  'linx-wordsmith': {
    name: 'Linx (Wordsmith)',
    emoji: '✍️',
    role: 'Documentation & Communication'
  },
  'product-acceptance-tester': {
    name: 'Product Acceptance Tester',
    emoji: '✅',
    role: 'Acceptance Testing & Validation'
  },
  'clive-prompt-strategist': {
    name: 'Clive (Prompt Strategist)',
    emoji: '🎯',
    role: 'Prompt Engineering & Strategy'
  },
  'liza-creative-companion': {
    name: 'Liza (Creative Companion)',
    emoji: '🎨',
    role: 'Creative Solutions & Ideation'
  }
};

class AgentTracker {
  constructor() {
    this.contributionsFile = path.join(process.cwd(), '.agent-contributions.json');
    this.contributions = {};
  }

  async loadContributions() {
    try {
      const data = await fs.readFile(this.contributionsFile, 'utf8');
      this.contributions = JSON.parse(data);
    } catch (err) {
      // File doesn't exist, start fresh
      this.contributions = {};
    }
  }

  async saveContributions() {
    await fs.writeFile(
      this.contributionsFile,
      JSON.stringify(this.contributions, null, 2)
    );
  }

  async trackContribution(prNumber, agentId, contribution) {
    if (!this.contributions[prNumber]) {
      this.contributions[prNumber] = {
        agents: {},
        timestamp: new Date().toISOString(),
        title: '',
        branch: this.getCurrentBranch()
      };
    }

    if (!this.contributions[prNumber].agents[agentId]) {
      this.contributions[prNumber].agents[agentId] = {
        contributions: [],
        firstContribution: new Date().toISOString()
      };
    }

    this.contributions[prNumber].agents[agentId].contributions.push({
      description: contribution,
      timestamp: new Date().toISOString()
    });

    await this.saveContributions();
  }

  getCurrentBranch() {
    try {
      return execSync('git branch --show-current', { encoding: 'utf8' }).trim();
    } catch {
      return 'unknown';
    }
  }

  generatePRComment(prNumber) {
    const pr = this.contributions[prNumber];
    if (!pr || Object.keys(pr.agents).length === 0) {
      return '## 🤖 No agent contributions tracked for this PR';
    }

    let comment = '## 🤖 Agent Contributions\n\n';
    comment += 'The following agents contributed to this PR:\n\n';
    
    // Create contribution table
    comment += '| Agent | Role | Contributions |\n';
    comment += '|-------|------|---------------|\n';

    for (const [agentId, data] of Object.entries(pr.agents)) {
      const agent = AGENTS[agentId] || { 
        name: agentId, 
        emoji: '🤖', 
        role: 'Unknown Role' 
      };
      
      const contributionList = data.contributions
        .map(c => `• ${c.description}`)
        .join('<br>');
      
      comment += `| ${agent.emoji} **${agent.name}** | ${agent.role} | ${contributionList} |\n`;
    }

    comment += '\n---\n';
    comment += '*🔧 Tracked by The Algorithm™ Agent Instrumentation System*';

    return comment;
  }

  async generateReport(prNumber) {
    const pr = this.contributions[prNumber];
    if (!pr) {
      console.log(`No contributions tracked for PR #${prNumber}`);
      return;
    }

    console.log(`\n📊 Agent Contribution Report for PR #${prNumber}`);
    console.log('=' .repeat(50));
    console.log(`Branch: ${pr.branch}`);
    console.log(`Started: ${pr.timestamp}`);
    console.log();

    for (const [agentId, data] of Object.entries(pr.agents)) {
      const agent = AGENTS[agentId] || { name: agentId, emoji: '🤖' };
      console.log(`${agent.emoji} ${agent.name}`);
      console.log('-'.repeat(40));
      
      for (const contribution of data.contributions) {
        const time = new Date(contribution.timestamp).toLocaleTimeString();
        console.log(`  [${time}] ${contribution.description}`);
      }
      console.log();
    }

    // Generate metrics
    console.log('📈 Collaboration Metrics:');
    console.log(`  • Total agents involved: ${Object.keys(pr.agents).length}`);
    console.log(`  • Total contributions: ${
      Object.values(pr.agents).reduce((sum, a) => sum + a.contributions.length, 0)
    }`);
    
    // Find most active agent
    let mostActive = null;
    let maxContributions = 0;
    for (const [agentId, data] of Object.entries(pr.agents)) {
      if (data.contributions.length > maxContributions) {
        mostActive = agentId;
        maxContributions = data.contributions.length;
      }
    }
    
    if (mostActive) {
      const agent = AGENTS[mostActive] || { name: mostActive, emoji: '🤖' };
      console.log(`  • Most active: ${agent.emoji} ${agent.name} (${maxContributions} contributions)`);
    }
  }
}

// CLI Interface
async function main() {
  const tracker = new AgentTracker();
  await tracker.loadContributions();

  const command = process.argv[2];
  const prNumber = process.argv[3];

  switch (command) {
    case 'track':
      const agentId = process.argv[4];
      const contribution = process.argv.slice(5).join(' ');
      await tracker.trackContribution(prNumber, agentId, contribution);
      console.log(`✅ Tracked contribution for ${agentId} on PR #${prNumber}`);
      break;

    case 'report':
      await tracker.generateReport(prNumber);
      break;

    case 'comment':
      const comment = tracker.generatePRComment(prNumber);
      console.log(comment);
      break;

    case 'clear':
      tracker.contributions = {};
      await tracker.saveContributions();
      console.log('🗑️ Cleared all contribution tracking data');
      break;

    default:
      console.log('Agent Contribution Tracker');
      console.log('Usage:');
      console.log('  node agent-tracker.js track <pr-number> <agent-id> <contribution>');
      console.log('  node agent-tracker.js report <pr-number>');
      console.log('  node agent-tracker.js comment <pr-number>');
      console.log('  node agent-tracker.js clear');
  }
}

if (require.main === module) {
  main().catch(console.error);
}

module.exports = { AgentTracker, AGENTS };