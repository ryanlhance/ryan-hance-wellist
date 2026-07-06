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
  "ev-13yrs": {"title": "13 years of client implementation", "text": "Six years running client work in film and TV, then seven more years of client implementation, consulting, and program management across startups, nationwide franchises, Delta Airlines, and Bayer."},
  "ev-film-producer": {"title": "Six productions at once, on time, on budget", "text": "Owned productions end to end as the client's point of contact, delivering on time and on budget while running an average of six concurrent productions, peaking at ten to twelve."},
  "ev-film-highstakes": {"title": "Million-dollar days were routine", "text": "As a film producer and assistant director, the responsibility of million-dollar days fell entirely on me — the plan, the crew, and the timeline all had to land correctly, every day. That was the normal rhythm of the job for six years."},
  "ev-onset-nexus": {"title": "Decision nexus for 40 productions", "text": "Was the on-set nexus for information, prioritization, and decision-making across 40 productions, coordinating thousands of crew, cast, and vendors live."},
  "ev-hamilton": {"title": "End-to-end client delivery for Hamilton Watches", "text": "Produced a branded film for Hamilton Watches and owned the client experience end to end, from scoping through delivery: 30+ crew, 20+ talent, eight locations, and ten-plus vendor partners — on time and on budget."},
  "ev-bayer-flux": {"title": "Three roles across Bayer in 18 months", "text": "My role at Bayer was constantly in flux, in the best way: UX lead for the farmer experience, design strategist for the operations platforms, then lead strategist for the generative AI effort — design leaders kept passing me around a 25,000-person division."},
  "ev-franchise-growth": {"title": "Client transformation opened a second location", "text": "Drove an operations and marketing transformation at a physical-health franchisee that opened the path to a second location."},
  "ev-delta-pm": {"title": "Primary client contact on a Delta engagement", "text": "Product Manager on a Delta Air Lines engagement: led a cross-cultural team spanning eight countries and nine disciplines, owned budget, timelines, and stakeholder relationships, and was the primary contact between client and team — presenting regularly in Delta's corporate rooms."},
  "ev-campus-carriers": {"title": "Pioneered a B2B2C program from scratch", "text": "Pioneered a new revenue line for a university logistics startup — a B2B2C education-as-a-service program spanning parents, students, and universities — owning it from market research through pre-launch partnerships."},
  "ev-dryland-pm-system": {"title": "Built the project management system twice", "text": "Designed the automations and information architecture of my startup's project management system — built it end to end in ClickUp, then rebuilt it in Monday.com because the mobile experience worked better for the field crew."},
  "ev-dryland-scale": {"title": "Scaled a startup to a profitable exit", "text": "Chief of staff who scaled Dryland, a construction-science startup, from one client to a profitable exit. One org redesign — detaching the CEO from day-to-day work — doubled revenue and quadrupled headcount in three months."},
  "ev-bayer-journey": {"title": "2,250 journey points across 27 teams", "text": "Facilitated a global journey mapping effort spanning North America, Europe, and Asia-Pacific — 2,250 journey points across 27 teams — that cut environmental toxin risk 70% and raised workplace safety 30% within two quarters."},
  "ev-service-blueprint": {"title": "Blueprints from startup to Fortune 500", "text": "Built service blueprints at every scale: Bayer's 20,000+ point global enterprise blueprint, and the 450-point blueprint of my own startup that became the information architecture for executive decision making."},
  "ev-ags-blueprint": {"title": "Blueprinted a franchise's tech-stack roadmap", "text": "Created an end-to-end service blueprint for a hospitality franchise to determine the tech stack roadmap for multi-location build-outs."},
  "ev-site-rebuild": {"title": "35% lift on a Fortune 500 site rebuild", "text": "UX Lead on Bayer's end-to-end customer site rebuild, from the public marketing pages through the logged-in customer portal — driving a 35% increase in product and service opportunities and leading user acceptance testing across the North American user base."},
  "ev-discovery": {"title": "Discovery starts every engagement", "text": "Discovery is where I start every engagement: ethnographic field research, stakeholder interviews, contextual inquiry, and journey mapping to turn workforce challenges into actionable solutions."},
  "ev-adoption": {"title": "2% to 26% adoption in two months", "text": "Took a Fortune 500's internal AI platform from 2% to 26% adoption in two months by building the playbook and training that got people to actually use it."},
  "ev-bananas": {"title": "Savannah Bananas' first sold-out season", "text": "First hire on the Savannah Bananas entertainment team: designed and executed the Fans First experiences and promotional campaigns the company standardized and scaled with, contributing to a 500% social awareness surge and the first sold-out season of 250,000 fans."},
  "ev-ai-playbook-langs": {"title": "AI playbook shipped in 20+ languages", "text": "Authored Bayer's AI Strategy Playbook and led its global dissemination in 20+ languages to thousands of internal users across business, engineering, design, and HR."},
  "ev-exec-alignment": {"title": "Sold Bayer execs on an AI build", "text": "Developed an agentic AI experience at Bayer and sold it internally to senior executives: months of workshops, demos, and one-on-one influencing, navigating the political complexity of enterprise decision making before getting the greenlight to build."},
  "ev-ags-consulting": {"title": "Strategic advisor to franchise leadership", "text": "As a consultant to franchisees and franchisors, I build relationships, influence, and drive the strategic alignment needed to get the opportunity to design new systems and lead enterprise transformation."},
  "ev-counseling-restructure": {"title": "Nationwide restructure, zero layoffs", "text": "Led the nationwide restructuring of a counseling franchise — grounded in ethnographic interviews with the corporate team and franchisees — and reorganized the corporate team with zero layoffs, using a research-driven decision tool I built."},
  "ev-playbooks": {"title": "I uncover and write the playbooks", "text": "An operations playbook that cut resource needs 60%, a startup playbook library that lifted efficiency 80%, and a Fortune 500 AI strategy playbook shipped in 20+ languages."},
  "ev-system-not-symptom": {"title": "I solve the system, not the symptom", "text": "I will spend an entire day on a single problem — solving the system instead of the symptom — because I know it will save days of time in the future."},
  "ev-metrics": {"title": "Fluent in adoption, time-to-launch, and satisfaction", "text": "Fluent in success metrics: OKRs, KPIs, adoption rate, time-to-launch, satisfaction. Drove measurable outcomes like a 35% lift in product and service opportunities and a 30% rise in workplace safety."},
  "ev-parallel": {"title": "Bayer 9-to-5, startup 5-to-9", "text": "Built a startup to a profitable exit while working Bayer full time — Bayer was my 9-to-5, the startup was my 5-to-9."},
  "ev-rampfast": {"title": "Four platforms shipped in year one", "text": "Walked into a Fortune 500 knowing nothing about agriculture and was shipping across four platforms within a year."},
  "ev-10industries": {"title": "10+ industries, hundreds of personas", "text": "Experience across 10+ industries and hundreds of niche personas; the service-design and operations skillset transfers to any business domain."},
  "ev-translator": {"title": "Translator between business, design, and engineering", "text": "Fluent in business, design, and engineering languages: translating business jargon to design requirements, engineering capabilities to business possibilities, and design visions to engineering roadmaps."},
  "ev-writing": {"title": "20–50 pages a week for a decade", "text": "A decade writing 20 to 50 pages a week, from user stories to executive strategy; authored Bayer's Universal Design Principles, adopted across every platform in the division."},
  "ev-facilitation": {"title": "Hundreds of workshops, 5 to 150 people", "text": "Facilitated hundreds of design thinking workshops from 5 to 150 people, and was selected by Miro as the sole Enterprise Advocate for all of Bayer — a company of ~100,000 people."},
  "ev-eq": {"title": "Gallup-certified Strengths Coach", "text": "Gallup-certified Strengths Coach trained in behavior and relationship psychology; taught empathy and emotional intelligence professionally through years of leadership development."},
  "ev-team-builder": {"title": "Teams that stay: 95% crew retention", "text": "I build teams that stay: roughly 95% crew retention across six years in film, a 67% year-over-year retention lift on a 250-person camp staff, and a startup hiring funnel that delivered 100% season-long retention of the hires who came through it."},
  "ev-workforce": {"title": "Workforce transformation, Fortune 500 to franchise", "text": "Workforce transformation in three settings: Bayer's employee experience platform, end-to-end people operations at my own startup, and the nationwide restructuring of a counseling franchise as a consultant."},
  "ev-wellbeing": {"title": "Years of wellbeing and behavioral work", "text": "Years of behavioral and wellbeing work: leadership development, emotional intelligence coaching, social-emotional learning programs, and cohort-based men's work."},
  "ev-scad": {"title": "An MBA crossed with service design", "text": "M.A. in Creative Business Leadership from SCAD's De Sole School of Business Innovation — essentially an MBA crossbred with service design, built for intrapreneurship and using design thinking to influence decision making."},
  "ev-travel": {"title": "Happy to travel", "text": "Would love to. 20 to 30% on the road genuinely works for me."},
  "ev-systems-guy": {"title": "System designer and implementer", "text": "I'm a systems guy — I can both architect and operationalize, so the strategic roadmap doesn't fall away after handoff. Ran ops for a 1,500-person summer camp and a university logistics startup — a 20-truck fleet, a 100,000-square-foot warehouse, 200+ seasonal staff — all while working in film and TV."},
  # ---- Portfolio pieces (public case studies) ----
  "ev-pf-blueprint-global": {"title": "Global Enterprise Service Blueprint", "text": "Bayer's 20,000+ point global service blueprint mapping tech, personas, and interactions across countries to surface redundancies and gaps."},
  "ev-pf-blueprint-local": {"title": "Local Enterprise Service Blueprint", "text": "A focused enterprise service blueprint mapping a business's systems and interaction points end to end."},
  "ev-pf-journey": {"title": "Global Journey Mapping Effort", "text": "A 27-team global journey map producing 2,250 journey points and new processes on a confidential European compliance project."},
  "ev-pf-cdp": {"title": "Customer Data Platform Roadmap", "text": "The use cases and roadmap, built from the customer-experience perspective, that anchored a Fortune 500's Customer Data Platform vendor selection."},
  "ev-pf-usertesting": {"title": "User Testing Strategic Recommendations", "text": "Using user research and testing to inform strategic product development on a supply chain platform."},
  "ev-pf-legacyux": {"title": "Legacy Software UX Strategy", "text": "Restructured forms, progress indicators, and language to make a legacy platform more efficient and usable."},
  "ev-pf-genai-playbook": {"title": "Generative A.I. Playbook", "text": "The AI strategy playbook that drove adoption from 2% to 26%, shipped in 20+ languages to thousands of users."},
  "ev-pf-platform-playbook": {"title": "Platform Design Playbook", "text": "A reusable playbook for designing and standing up new platforms."},
  "ev-pf-personas": {"title": "A.I. Persona Prototypes", "text": "Agentic AI personas wired into Microsoft Teams — built before commercial AI integrations existed and launched across multiple company-wide platforms — so teams could interview user models they couldn't otherwise reach."},
  "ev-pf-ai-roadmap": {"title": "A.I. Product Roadmap", "text": "Product roadmap for a Fortune 500's internal AI platform, defining the use cases and the path to adoption."},
  "ev-pf-prompt": {"title": "Prompt Engineering Strategic Design", "text": "A prompt engineering approach and template that let non-technical stakeholders across the company use generative AI effectively for the first time."},
  "ev-pf-eraf": {"title": "Systems Flow (ERAF) Map", "text": "A systems-flow map of 100+ interaction points that helped siloed teams see their role in the larger business — and kept employees who were ready to quit over 'bad communication.'"},
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
       ["ev-film-producer", "ev-film-highstakes", "ev-hamilton", "ev-delta-pm"]),
    " — ",
    ph("p-measurable-roi", "ensuring each employer sees measurable ROI",
       ["ev-metrics", "ev-adoption", "ev-site-rebuild", "ev-franchise-growth", "ev-dryland-scale"]),
    " and every employee gets the personalized support they need."
  ]},
  {"type": "p", "segments": [
    "We're looking for a ",
    ph("p-strategic-operator", "sharp, strategic operator who thrives in complexity",
       ["ev-systems-guy", "ev-bayer-flux", "ev-onset-nexus", "ev-film-highstakes", "ev-service-blueprint"]),
    ", ",
    ph("p-clarity", "communicates with clarity", ["ev-writing", "ev-translator", "ev-facilitation"]),
    ", and ",
    ph("p-systems-scale", "loves building systems that scale",
       ["ev-playbooks", "ev-system-not-symptom", "ev-service-blueprint", "ev-dryland-pm-system", "ev-pf-blueprint-global", "ev-pf-eraf"]),
    ". If you're excited by the challenge of ",
    ph("p-highgrowth-standup", "standing up new client programs in a high-growth environment",
       ["ev-parallel", "ev-dryland-scale", "ev-campus-carriers", "ev-bananas"]),
    " — this role is for you."
  ]},

  {"type": "h2", "text": "What You'll Own"},

  {"type": "h3", "text": "End-to-End Implementation Leadership"},
  {"type": "li", "segments": [
     "Serve as the ",
     ph("p-primary-lead", "primary lead for new client deployments",
        ["ev-delta-pm", "ev-film-producer", "ev-hamilton", "ev-ags-consulting"]),
     " — ",
     ph("p-kickoff-launch", "owning everything from kickoff to launch",
        ["ev-hamilton", "ev-film-producer", "ev-campus-carriers", "ev-pf-personas"]),
     "."]},
  {"type": "li", "segments": [
     ph("p-tailored-plans", "Build tailored implementation plans",
        ["ev-service-blueprint", "ev-ags-blueprint", "ev-pf-blueprint-global", "ev-pf-blueprint-local"]),
     " that ",
     ph("p-align-workforce", "align with each employer's workforce needs",
        ["ev-discovery", "ev-bayer-journey", "ev-workforce"]),
     ", benefits portfolio, and engagement goals."]},
  {"type": "li", "segments": [
     ph("p-partner-stakeholders", "Partner closely with internal stakeholders",
        ["ev-facilitation", "ev-translator", "ev-onset-nexus", "ev-dryland-scale"]),
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
        ["ev-site-rebuild", "ev-pf-legacyux", "ev-service-blueprint", "ev-ags-blueprint", "ev-pf-cdp"]),
     " that ",
     ph("p-reflect-brand", "reflect each client's brand, culture, and priorities",
        ["ev-site-rebuild", "ev-hamilton", "ev-bananas", "ev-pf-blueprint-local"]),
     "."]},
  {"type": "li", "segments": [
     ph("p-discovery-convos", "Lead discovery conversations",
        ["ev-discovery", "ev-counseling-restructure", "ev-facilitation", "ev-bayer-journey", "ev-pf-journey"]),
     " to understand workforce challenges and ",
     ph("p-actionable-solutions", "translate those into actionable solutions",
        ["ev-discovery", "ev-pf-personas", "ev-pf-eraf", "ev-pf-usertesting"]),
     "."]},
  {"type": "li", "segments": [
     "Collaborate with client stakeholders to develop ",
     ph("p-launch-campaigns", "launch campaigns",
        ["ev-adoption", "ev-bananas"]),
     ", email communications, and ",
     ph("p-engagement-strategies", "internal engagement strategies",
        ["ev-adoption", "ev-ai-playbook-langs", "ev-writing", "ev-pf-eraf"]),
     "."]},

  {"type": "h3", "text": "Program Activation & Optimization"},
  {"type": "li", "segments": [
     ph("p-activation-tactics", "Implement and refine activation tactics",
        ["ev-bananas", "ev-ai-playbook-langs", "ev-pf-prompt"]),
     " — such as segmented outreach, referral prompts, and tailored content — to ",
     ph("p-drive-adoption", "drive user adoption",
        ["ev-adoption", "ev-pf-genai-playbook", "ev-pf-ai-roadmap"]),
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
        ["ev-exec-alignment", "ev-ags-consulting", "ev-counseling-restructure", "ev-workforce"]),
     " — ensuring that each program delivers value and exceeds expectations."]},

  {"type": "h3", "text": "Scalable Systems & Process Excellence"},
  {"type": "li", "segments": [
     ph("p-codify-playbooks", "Codify implementation workflows, toolkits, and playbooks",
        ["ev-playbooks", "ev-system-not-symptom", "ev-dryland-pm-system", "ev-pf-platform-playbook", "ev-pf-genai-playbook"]),
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
        ["ev-dryland-scale", "ev-team-builder"]),
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
        ["ev-film-highstakes", "ev-onset-nexus", "ev-delta-pm", "ev-hamilton", "ev-bayer-journey"]),
     "."]},
  {"type": "li", "segments": [
     "Experience ",
     ph("p-enterprise-rel", "navigating enterprise client relationships",
        ["ev-exec-alignment", "ev-ags-consulting", "ev-delta-pm"]),
     " and ",
     ph("p-strategic-alignment", "driving strategic alignment with senior executives",
        ["ev-exec-alignment", "ev-counseling-restructure", "ev-delta-pm"]),
     "."]},
  {"type": "li", "segments": [
     "A ",
     ph("p-process-mindset", "process mindset",
        ["ev-system-not-symptom", "ev-playbooks", "ev-dryland-pm-system"]),
     " — you make it easier to get things done again."]},
  {"type": "li", "segments": [
     "Comfort in ",
     ph("p-highgrowth-lean", "high-growth, resource-constrained environments where speed and adaptability matter",
        ["ev-parallel", "ev-rampfast", "ev-bayer-flux", "ev-dryland-scale"]),
     "."]},
  {"type": "li", "segments": [
     "Strong ",
     ph("p-communication", "communication and stakeholder management skills",
        ["ev-writing", "ev-facilitation", "ev-translator", "ev-eq"]),
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
    "candidate_lede": "This is collected notes and resume points on Ryan Hance's career experience mapped to the Wellist job description.",
    "candidate_stat": "Hover over any underlined phrase and select it to see Ryan's experience related to the ask.",
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
