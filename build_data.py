#!/usr/bin/env python3
"""Generates data.json for the Wellist fit-map page.
Single source of truth: edit this, run `python3 build_data.py`, and data.json
is rewritten. (Or just edit data.json directly — this is a convenience.)
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))

# ---- Portfolio public URLs (piece -> hance.work case study) ----
PF = {
    "ev-pf-blueprint-local":   "https://www.hance.work/Local-Enterprise-Level-Service-Blueprint-74f9ecfa9f4a4873be1b909a7f5e37d8?pvs=25",
    "ev-pf-eraf":              "https://www.hance.work/Systems-Flow-ERAF-Map-74cfa7e910564777a9883a55f066d4f9?pvs=25",
    "ev-pf-blueprint-global":  "https://www.hance.work/Global-Enterprise-Level-Service-Blueprint-cd937db4cb344b318bae4c6d1e7ca9fa?pvs=25",
    "ev-pf-journey":           "https://www.hance.work/Global-Journey-Mapping-Effort-228e643935ea43aab50ee95d8f56305f?pvs=25",
    "ev-pf-cdp":               "https://www.hance.work/Customer-Data-Platform-Roadmap-0d65a3c99943497e9c969160e33742a2?pvs=25",
    "ev-pf-ai-roadmap":        "https://www.hance.work/A-I-Product-Roadmap-d042f4d986e5441bbb80b5e5ea4bd018?pvs=25",
    "ev-pf-platform-playbook": "https://www.hance.work/Platform-Design-Playbook-838ea8da681f4577bce28f0ea7e30b67?pvs=25",
    "ev-pf-genai-playbook":    "https://www.hance.work/Generative-A-I-Playbook-bb68ca8c80d840e5be083136a0b88f92?pvs=25",
    "ev-pf-personas":          "https://www.hance.work/A-I-Persona-Prototypes-43575337f52c4cecaf4fdd871e5aa41e?pvs=25",
    "ev-pf-usertesting":       "https://www.hance.work/User-Testing-Strategic-Recommendations-9f073d6ea0bb4bd1bef08d176895dd10?pvs=25",
    "ev-pf-legacyux":          "https://www.hance.work/Legacy-Software-UX-Strategy-e189dab0fccc4d088f0f8e2a22b009a9?pvs=25",
    "ev-pf-prompt":            "https://www.hance.work/Prompt-Engineering-Strategic-Design-40891c882c00477e936743a5d0657ddc?pvs=25",
}

# ---- Evidence (title + text shown to the reader; source kept for your own reference, never displayed) ----
evidence = {
  "ev-13yrs": {"title": "13 years of client implementation", "text": "About 13 years of exactly this: 6 running client work in film and TV, then 7 more across startups, nationwide franchises, Delta, and Bayer. Implementation is the whole job, not a part of it."},
  "ev-film-producer": {"title": "Lead Producer & AD", "text": "Owned productions end to end as the client's point of contact, delivering on time and on budget while running an average of six concurrent productions, peaking at ten to twelve."},
  "ev-film-highstakes": {"title": "Million-dollar days", "text": "As a producer and AD, a normal Wednesday meant a million-dollar day riding on me getting the plan, crew, and timeline right. High stakes at speed is where I get calm, not rattled."},
  "ev-onset-nexus": {"title": "On-set decision nexus", "text": "Was the on-set nexus for information, prioritization, and decision-making across 40 productions, coordinating thousands of crew, cast, and vendors live."},
  "ev-delta-pm": {"title": "Delta engagement, Product Manager", "text": "Product Manager on a Delta engagement: led a cross-cultural team from eight countries and nine disciplines, managed budget, timelines, resources, and stakeholder relationships, and was the primary contact between client and team, presenting to corporate."},
  "ev-campus-carriers": {"title": "New B2B2C program launch", "text": "Pioneered a new revenue line by architecting a B2B2C education-as-a-service structure spanning parents, students, and universities, from market research through pre-launch partnerships."},
  "ev-dryland-pm-system": {"title": "PM system build", "text": "Designed the automations and information architecture of Dryland's project management system, building it end to end in ClickUp before rebuilding in Monday for the field team."},
  "ev-dryland-scale": {"title": "Zero to profitable exit", "text": "Chief of staff who scaled Dryland from one client to a profitable exit, doubling revenue and quadrupling headcount by redesigning the operating model."},
  "ev-bayer-journey": {"title": "Global journey mapping", "text": "Facilitated a global journey mapping effort across NA, EMEA, and APAC that produced 2,250 journey points across 27 teams."},
  "ev-service-blueprint": {"title": "Enterprise service blueprints", "text": "Built service blueprints at every scale: Bayer's 20,000+ point global enterprise blueprint and Dryland's 450-point operating system that became the executive decision architecture."},
  "ev-ags-blueprint": {"title": "Franchise tech-stack roadmap", "text": "Created an end-to-end service blueprint for a hospitality franchise to determine the tech stack roadmap for multi-location build-outs."},
  "ev-site-rebuild": {"title": "Customer site rebuild", "text": "UX Lead on Bayer's end-to-end customer site rebuild across pre-auth and post-auth surfaces, driving a 35% increase in product and service opportunities and leading UAT across the NA user base."},
  "ev-discovery": {"title": "Discovery and contextual research", "text": "Discovery is core craft: ethnographic field research, stakeholder interviews, contextual inquiry, and journey mapping to turn workforce challenges into actionable solutions."},
  "ev-adoption": {"title": "2% to 26% adoption in two months", "text": "Took a Fortune 500's internal AI platform from 2% to 26% adoption in two months, mostly by building the playbook and training that got people to actually use it. That is the same adoption problem this role owns."},
  "ev-bananas": {"title": "Savannah Bananas, Fans First activation", "text": "First hire on the Savannah Bananas entertainment team: designed the Fans First experiences the company scaled with, contributing to a 500% social awareness surge and the first sold-out season of 250,000 fans."},
  "ev-ai-playbook-langs": {"title": "AI playbook in 20+ languages", "text": "Authored Bayer's AI Strategy Playbook and led its global dissemination in 20+ languages to thousands of internal users across business, engineering, design, and HR."},
  "ev-exec-alignment": {"title": "Aligning senior executives", "text": "Sold an agentic AI build to Bayer senior execs: months of workshops, demos, and one-on-ones through real enterprise politics before the greenlight. I earn the alignment before I ever get to build."},
  "ev-ags-consulting": {"title": "Consulting alignment", "text": "As a consultant to franchisees and franchisors, I build the relationships and strategic alignment needed to earn the right to redesign their systems and lead enterprise transformation."},
  "ev-counseling-restructure": {"title": "Nationwide restructuring", "text": "Led the nationwide restructuring of a counseling franchise and reorganized the corporate team with zero layoffs, using a research-driven decision tool I built."},
  "ev-playbooks": {"title": "Codifies work into playbooks", "text": "I codify what I build into playbooks and toolkits so it scales: Dryland's playbook library (+80% efficiency), an ops playbook (-60% resource need), and Bayer's AI playbook in 20+ languages."},
  "ev-system-not-symptom": {"title": "Fixes the system, not the symptom", "text": "I fix the system, not the symptom. I'll spend a whole day on the underlying process so the next person, or the AI, gets it right every time. Repeatable playbooks are how I work."},
  "ev-metrics": {"title": "Runs on success metrics", "text": "Fluent in success metrics: OKRs, KPIs, adoption rate, time-to-launch, satisfaction. Drove measurable outcomes like a 35% lift in opportunities and a 30% rise in workplace safety."},
  "ev-parallel": {"title": "Startup and F500 in parallel", "text": "Built a startup to a profitable exit while working Bayer full time. I ramp fast and travel light."},
  "ev-rampfast": {"title": "Fast ramp in a new domain", "text": "Walked into a Fortune 500 knowing nothing about agriculture and was shipping value across four platforms within a year."},
  "ev-10industries": {"title": "Cross-vertical range", "text": "Experience across 10+ industries and hundreds of niche personas; the service-design and operations skillset transfers to any business domain."},
  "ev-writing": {"title": "A decade of writing", "text": "A decade writing 20 to 50 pages a week, from user stories to executive strategy; authored Bayer's Universal Design Principles adopted across every platform."},
  "ev-facilitation": {"title": "Workshop facilitation", "text": "Facilitated hundreds of design thinking workshops from 5 to 150 people, and was selected as Bayer's single Miro Enterprise Advocate."},
  "ev-eq": {"title": "EQ and psychology", "text": "Gallup Strengths Coach trained in behavior and relationship psychology; taught empathy and EQ professionally through years of leadership development."},
  "ev-workforce": {"title": "Workforce transformation", "text": "Workforce transformation across Bayer's employee experience platform, people ops at Dryland, and the nationwide restructuring of a franchise at AGS."},
  "ev-wellbeing": {"title": "Wellbeing work", "text": "Years of behavioral and wellbeing work: leadership development, EQ coaching, SEL programs, and men's cohort work."},
  "ev-scad": {"title": "SCAD master's degree", "text": "M.A. in Creative Business Leadership from SCAD's De Sole School of Business Innovation: an MBA fused with design thinking, built to turn research into strategy. Reads almost like a description of this role."},
  "ev-travel": {"title": "Happy to travel", "text": "Genuinely happy to travel 20-30%. I like being where the work and the people are."},
  "ev-systems-guy": {"title": "A systems operator", "text": "I'm a systems person. I design how something works, then operate it so it actually delivers. Ran ops for a 1,500-person summer camp and a university logistics startup, all while working film."},
  # ---- Portfolio pieces (public case studies) ----
  "ev-pf-blueprint-global": {"title": "Global Enterprise Service Blueprint", "text": "Bayer's 20,000+ point global service blueprint mapping tech, personas, and interactions across countries to surface redundancies and gaps."},
  "ev-pf-blueprint-local": {"title": "Local Enterprise Service Blueprint", "text": "A focused enterprise service blueprint mapping a business's systems and interaction points end to end."},
  "ev-pf-journey": {"title": "Global Journey Mapping Effort", "text": "A 27-team global journey map producing 2,250 journey points and new processes on a large EU project."},
  "ev-pf-cdp": {"title": "Customer Data Platform Roadmap", "text": "CDP use cases and roadmap from the customer-experience perspective that anchored an enterprise vendor selection."},
  "ev-pf-usertesting": {"title": "User Testing Strategic Recommendations", "text": "Using user research and testing to inform strategic product development on a supply chain platform."},
  "ev-pf-legacyux": {"title": "Legacy Software UX Strategy", "text": "Restructured forms, progress indicators, and language to make a legacy platform more efficient and usable."},
  "ev-pf-genai-playbook": {"title": "Generative A.I. Playbook", "text": "The AI strategy playbook that took internal adoption from 2% to 26%, shipped in 20+ languages."},
  "ev-pf-platform-playbook": {"title": "Platform Design Playbook", "text": "A reusable playbook for designing and standing up platforms in a repeatable way."},
  "ev-pf-personas": {"title": "A.I. Persona Prototypes", "text": "Agentic AI personas wired into Microsoft Teams so teams could interview user models they couldn't otherwise reach."},
  "ev-pf-ai-roadmap": {"title": "A.I. Product Roadmap", "text": "Product roadmap for an internal AI/LLM effort, defining use cases and the path to adoption."},
  "ev-pf-prompt": {"title": "Prompt Engineering Strategic Design", "text": "A prompt engineering approach and template that let non-technical stakeholders use LLMs effectively."},
  "ev-pf-eraf": {"title": "Systems Flow (ERAF) Map", "text": "An ERAF systems-flow map helping siloed teams see their role in the larger business system."},
}
# attach portfolio links
for k, url in PF.items():
    evidence[k]["link"] = url

def ph(pid, text, ev):
    return {"id": pid, "text": text, "evidence": ev}

# ---- The job description, as real prose with inline highlighted phrases ----
jd_prose = [
  {"type": "p", "segments": [
    "At Wellist, we're helping employers deliver the right resources at the right time — so employees can feel supported through every life moment, and HR leaders can maximize the value of their investments."
  ]},
  {"type": "p", "segments": [
    "As our ", {"b": "Senior Manager, Experience Strategy & Implementation"},
    ", you'll play a mission-critical role in ",
    ph("p-launch-programs", "launching new employer programs",
       ["ev-13yrs", "ev-delta-pm", "ev-campus-carriers", "ev-dryland-scale"]),
    ". From ",
    ph("p-fortune1000", "onboarding Fortune 1000 clients",
       ["ev-delta-pm", "ev-site-rebuild", "ev-exec-alignment", "ev-10industries", "ev-pf-cdp"]),
    " to ",
    ph("p-activation-strategies", "driving tailored activation strategies",
       ["ev-adoption", "ev-bananas", "ev-ai-playbook-langs"]),
    ", you'll be responsible for ",
    ph("p-launch-success", "making every launch a success",
       ["ev-film-producer", "ev-film-highstakes", "ev-delta-pm"]),
    " — ",
    ph("p-measurable-roi", "ensuring each employer sees measurable ROI",
       ["ev-metrics", "ev-adoption", "ev-dryland-scale"]),
    " and every employee gets the personalized support they need."
  ]},
  {"type": "p", "segments": [
    "We're looking for a ",
    ph("p-strategic-operator", "sharp, strategic operator who thrives in complexity",
       ["ev-systems-guy", "ev-onset-nexus", "ev-film-highstakes"]),
    ", ",
    ph("p-clarity", "communicates with clarity", ["ev-writing", "ev-facilitation"]),
    ", and ",
    ph("p-systems-scale", "loves building systems that scale",
       ["ev-playbooks", "ev-system-not-symptom", "ev-service-blueprint", "ev-pf-blueprint-global", "ev-pf-eraf"]),
    ". If you're excited by the challenge of ",
    ph("p-highgrowth-standup", "standing up new client programs in a high-growth environment",
       ["ev-parallel", "ev-dryland-scale", "ev-campus-carriers"]),
    " — this role is for you."
  ]},

  {"type": "h2", "text": "What You'll Own"},

  {"type": "h3", "text": "End-to-End Implementation Leadership"},
  {"type": "li", "segments": [
     "Serve as the ",
     ph("p-primary-lead", "primary lead for new client deployments",
        ["ev-delta-pm", "ev-film-producer", "ev-campus-carriers"]),
     " — ",
     ph("p-kickoff-launch", "owning everything from kickoff to launch",
        ["ev-film-producer", "ev-campus-carriers"]),
     "."]},
  {"type": "li", "segments": [
     ph("p-tailored-plans", "Build tailored implementation plans",
        ["ev-service-blueprint", "ev-ags-blueprint", "ev-pf-blueprint-global", "ev-pf-blueprint-local"]),
     " that ",
     ph("p-align-workforce", "align with each employer's workforce needs",
        ["ev-discovery", "ev-bayer-journey"]),
     ", benefits portfolio, and engagement goals."]},
  {"type": "li", "segments": [
     ph("p-partner-stakeholders", "Partner closely with internal stakeholders",
        ["ev-facilitation", "ev-dryland-scale", "ev-onset-nexus"]),
     " (Support, Product, Directory, and Activation) to ",
     ph("p-coordinated-execution", "ensure coordinated execution",
        ["ev-onset-nexus", "ev-pf-eraf"]),
     "."]},
  {"type": "li", "segments": [
     ph("p-track-milestones", "Track project milestones and dependencies",
        ["ev-dryland-pm-system", "ev-onset-nexus"]),
     ", manage risks, and ",
     ph("p-timelines", "keep timelines on track with precision",
        ["ev-film-producer", "ev-film-highstakes"]),
     "."]},

  {"type": "h3", "text": "Client Strategy & Customization"},
  {"type": "li", "segments": [
     ph("p-platform-config", "Design platform configurations and directory customization plans",
        ["ev-site-rebuild", "ev-pf-legacyux", "ev-service-blueprint", "ev-ags-blueprint"]),
     " that ",
     ph("p-reflect-brand", "reflect each client's brand, culture, and priorities",
        ["ev-site-rebuild", "ev-pf-blueprint-local"]),
     "."]},
  {"type": "li", "segments": [
     ph("p-discovery-convos", "Lead discovery conversations",
        ["ev-discovery", "ev-facilitation", "ev-pf-journey", "ev-bayer-journey"]),
     " to understand workforce challenges and ",
     ph("p-actionable-solutions", "translate those into actionable solutions",
        ["ev-discovery", "ev-pf-usertesting"]),
     "."]},
  {"type": "li", "segments": [
     "Collaborate with client stakeholders to develop ",
     ph("p-launch-campaigns", "launch campaigns",
        ["ev-adoption", "ev-bananas"]),
     ", email communications, and ",
     ph("p-engagement-strategies", "internal engagement strategies",
        ["ev-adoption", "ev-writing", "ev-ai-playbook-langs"]),
     "."]},

  {"type": "h3", "text": "Program Activation & Optimization"},
  {"type": "li", "segments": [
     ph("p-activation-tactics", "Implement and refine activation tactics",
        ["ev-bananas", "ev-ai-playbook-langs", "ev-pf-personas"]),
     " — such as segmented outreach, referral prompts, and tailored content — to ",
     ph("p-drive-adoption", "drive user adoption",
        ["ev-adoption", "ev-pf-genai-playbook"]),
     "."]},
  {"type": "li", "segments": [
     ph("p-analyze-data", "Analyze client performance data and user feedback",
        ["ev-metrics", "ev-pf-cdp", "ev-pf-usertesting", "ev-discovery"]),
     " to ",
     ph("p-early-wins", "identify early wins and opportunities for improvement",
        ["ev-metrics", "ev-site-rebuild"]),
     "."]},
  {"type": "li", "segments": [
     "Serve as a ",
     ph("p-advisor-hr", "strategic advisor to HR and Benefits leaders",
        ["ev-exec-alignment", "ev-ags-consulting", "ev-workforce"]),
     " — ensuring that each program delivers value and exceeds expectations."]},

  {"type": "h3", "text": "Scalable Systems & Process Excellence"},
  {"type": "li", "segments": [
     ph("p-codify-playbooks", "Codify implementation workflows, toolkits, and playbooks",
        ["ev-playbooks", "ev-system-not-symptom", "ev-pf-platform-playbook", "ev-pf-genai-playbook"]),
     " to ",
     ph("p-future-scale", "support future scale",
        ["ev-dryland-scale", "ev-playbooks"]),
     "."]},
  {"type": "li", "segments": [
     ph("p-success-metrics", "Define and track key success metrics",
        ["ev-metrics", "ev-adoption"]),
     " (e.g., time to launch, adoption rates, satisfaction scores)."]},
  {"type": "li", "segments": [
     ph("p-implementation-framework", "Contribute to Wellist's implementation framework",
        ["ev-playbooks", "ev-service-blueprint", "ev-pf-platform-playbook", "ev-pf-eraf"]),
     " and play a key role in ",
     ph("p-grow-success", "growing our client success function",
        ["ev-dryland-scale"]),
     "."]},

  {"type": "h2", "text": "What You Bring"},
  {"type": "li", "segments": [
     "5+ years of experience in ",
     ph("p-5years", "client implementation, consulting, or program management",
        ["ev-13yrs", "ev-film-producer", "ev-delta-pm", "ev-ags-consulting"]),
     "."]},
  {"type": "li", "segments": [
     "Proven ability to lead ",
     ph("p-complex-crossfunctional", "complex, cross-functional projects with tight timelines and high stakes",
        ["ev-film-highstakes", "ev-onset-nexus", "ev-delta-pm"]),
     "."]},
  {"type": "li", "segments": [
     "Experience ",
     ph("p-enterprise-rel", "navigating enterprise client relationships",
        ["ev-ags-consulting", "ev-exec-alignment"]),
     " and ",
     ph("p-strategic-alignment", "driving strategic alignment with senior executives",
        ["ev-exec-alignment", "ev-counseling-restructure"]),
     "."]},
  {"type": "li", "segments": [
     "A ",
     ph("p-process-mindset", "process mindset",
        ["ev-system-not-symptom", "ev-playbooks"]),
     " — you make it easier to get things done again."]},
  {"type": "li", "segments": [
     "Comfort in ",
     ph("p-highgrowth-lean", "high-growth, resource-constrained environments where speed and adaptability matter",
        ["ev-parallel", "ev-rampfast", "ev-dryland-scale"]),
     "."]},
  {"type": "li", "segments": [
     "Strong ",
     ph("p-communication", "communication and stakeholder management skills",
        ["ev-writing", "ev-facilitation", "ev-eq"]),
     " — written, verbal, and interpersonal."]},
  {"type": "li", "segments": [
     "Experience in ",
     ph("p-hrtech-digitalhealth", "HR Tech, workforce transformation, or digital health",
        ["ev-workforce", "ev-wellbeing"]),
     " strongly preferred."]},
  {"type": "li", "segments": [
     ph("p-masters", "Master's degree in Business or related field",
        ["ev-scad"]),
     " a plus."]},
  {"type": "li", "segments": [
     "Willingness to ",
     ph("p-travel", "travel 20–30% as needed",
        ["ev-travel"]),
     "."]},
]

data = {
  "meta": {
    "candidate": "Ryan Hance",
    "portfolio": "https://www.hance.work/",
    "note": "Pure renderer input. Edit copy here (or in build_data.py). Each highlighted phrase carries the evidence ids that back it; evidence is a shared dictionary."
  },
  "job": {
    "company": "Wellist",
    "role": "Senior Manager, Experience Strategy & Implementation",
    "employment": "Hybrid",
    "location": "Boston, MA",
    "url": "https://job-boards.greenhouse.io/wellist/jobs/8604140002",
    "tab_title": "Ryan Hance · Fit Map",
    "candidate_kicker": "Ryan Hance · Fit Map",
    "candidate_lede": "This is the Wellist job description. Every underlined phrase maps to real, specific experience — hover one to see it's clickable, then click to see the proof.",
    "candidate_stat": "Every underlined phrase below opens the specific, real experience behind it.",
  },
  "evidence": evidence,
  "jd_prose": jd_prose,
}

out = os.path.join(HERE, "data.json")
with open(out, "w") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# quick self-check: every referenced evidence id exists
ids = set()
for b in jd_prose:
    for seg in b.get("segments", []):
        if isinstance(seg, dict) and "evidence" in seg:
            ids.update(seg["evidence"])
missing = [i for i in ids if i not in evidence]
print("Wrote", out)
print("phrases:", sum(1 for b in jd_prose for s in b.get("segments", []) if isinstance(s, dict) and "id" in s))
print("evidence items:", len(evidence))
print("missing evidence refs:", missing or "none")
