# Career — history & timeline

Sources: CV (`Alexis-Simpson-CV.docx`, Sep 2026) + LinkedIn ([alexis-simpson-35716189](https://www.linkedin.com/in/alexis-simpson-35716189/)) + life context.

## Snapshot (Sep 2026)

- **Senior Software Architect at Trimble** (2022–present): architect for a petabyte-scale, multi-tenant geospatial big data platform — ~100 enterprise customers, thousands of end users, 10+ services across 8 AWS regions. Owns the infrastructure, deployment and security patterns used by ~40 engineers across 5–10 teams. Lead architect on Trimble's **FedRAMP programme**. Top 5% NZ salary.
- CV positioning line: *"Cloud and software architect with 15 years in enterprise IT, the last eight designing hyperscale systems across AWS, Azure and GCP."*
- Links: [leet.cloud](https://leet.cloud) · [github.com/vendablefall](https://github.com/vendablefall)
- **Sep 2026:** applying for jobs — Auckland roles that would be a career step up; either take one she likes or use as leverage for more pay. Weighing career vs the Wellington community (see `journal/2026-09-04.md`).

## Timeline

- **2010 — Bachelor of Commerce, University of Canterbury** (Christchurch). Double major: Management Science (statistics, supply chain logistics) and Management.
- **2011–2018 — CITEC, Brisbane.** Service Desk → Cloud Specialist over seven years. Appointed **AWS Cloud Warrior for the Queensland Government** (2018); lead architect on an AWS WorkSpaces proof of concept; designed highly available VMware environments for government agencies; built a PowerShell automation/reporting platform; trained and mentored new team members.
  - **Concurrent: professional rugby league, Queensland Cup (2011–2014)** — full-time IT career alongside professional sport, the whole time. Sunshine Coast Sea Eagles (2011–2012), then **Redcliffe Dolphins (2013–2014)**, playing front row forward. In 2013 the other starting prop was **Petero Civoniceva**, one of the greatest of all time, playing his final season at his junior club. In **2015** she played one season of senior non-professional footy with the **West Mitchelton Panthers** (two grades lower) and **won the grand final — her last game ever**. Bonus: as a 2012 starter for the Sea Eagles, she's a playable character in *Rugby League Live 2* (Big Ant Studios, 2012, PS3/Xbox 360), which licensed the Queensland Cup rosters. (Her personal story: after Mark's death she quit rugby and the training hours became study hours — the certification blitz below is the visible record.)
- **2017–2019 — Certification blitz:** VMware VCP6-DCV, PRINCE2 Practitioner, AWS Associate ×3 (2017); AWS Solutions Architect Professional, AWS DevOps Engineer Professional, AWS Advanced Networking Specialty (2018); Google Cloud Professional Cloud Architect + Professional Data Engineer (2019).
- **2018–2019 — Senior Cloud Consultant, CloudTrek → Deloitte, Brisbane** (CloudTrek acquired by Deloitte Australia, Sep 2018). Led multi-disciplinary cloud teams delivering enterprise AWS architecture: serverless data lakes, database migrations, security/DevOps governance, reusable automation frameworks.
- **2019–2020 — Senior Data & Cloud Engineer, Datisan, Brisbane.** GCP data lakes and serverless environments for enterprise clients; ML model development and deployment; Google marketing stack consulting; ran client training workshops and led engagements end to end.
- **2020–2021 — Senior DevOps Engineer, BinderPOS** (Tauranga company; the move back to NZ — worked fully remote from **Arrowtown**, where she and Bridget settled to be near family and build the housebus). Kubernetes platform on GCP for a SaaS point-of-sale product serving 100+ retailers; GitLab CI/CD replacing manual deployment.
- **2020–2022 — leet.cloud (sole proprietor, concurrent).** Independent cloud consultancy: GCP data lake and IaC architecture, AWS CI/CD design, DevOps advisory, cloud security review for 10+ clients. The site ([leet.cloud](https://leet.cloud)) doubles as her portfolio and hosts **[Pebkac](https://blog.leet.cloud)** — the IT blog she started in the certification years to get ahead (GlusterFS, AWS VPC/API Gateway deep dives, the data-engineering pivot post); dormant for a long while now.
- **2021 — Senior Cloud Architect, CFB Group.** Led a team of 5 DevOps engineers; Kubernetes platforms on GCP for a global card trading marketplace (millions of SKUs) plus a live financial transaction application; moved 4 teams onto GitLab CI/CD.
- **2021–2022 — Co-Creator, AiVatar (concurrent)** — *the NFT project*, a collaboration with photographer **Trey Ratcliff** ([aivatar.io](https://aivatar.io)): ~6,000 AI avatars framed as "a GPT-3 time capsule reflecting the progression towards self-awareness." Lexi was **principal architect and developer** — smart contracts and minting infrastructure (6,666 mints in the first 24 hours, sold out in 6 weeks — the ~$1M day), the generative AI pipeline that produced the collection, and serverless AWS infrastructure that absorbed launch-day traffic and is still running four years on. $250k+ of the proceeds funded her surgeries.
- **2022–present — Senior Software Architect, Trimble.** Started the same year she came out (Jan 2022) and began medical transition (Mar 2022) — carried the role through all of it. Highlights:
  - Architected **two successive generations** of the platform: first re-platformed from team-managed EC2 to Azure serverless (Functions, Cosmos DB, Storage), then designed and delivered its AWS replacement — multi-region EKS across 8 regions, fully Terraform-provisioned, released via GitHub Actions. Currently leading the production migration from Azure, mostly zero-downtime.
  - Introduced Infrastructure as Code to the organisation (ARM, then Terraform as the company-wide standard).
  - **Lead architect, FedRAMP programme**; platform also operates under SOC 2, ISO 27001 and GDPR, with automated security scanning in every pipeline.
  - Built the platform foundation ~40 engineers consume daily: pipeline templates, Terraform modules, environment provisioning, release governance, security gates, reference patterns.
  - Designed cache-first global delivery of ML-rendered 3D tilesets (CloudFront + Azure Front Door + Cloudflare multi-tier caching) so petabyte-scale point-cloud data streams to browsers without origin load scaling with users.
  - **AI mentor for the organisation:** corporate governance for AI coding agents (MCP servers, repo-level rules, least-privilege RBAC), AI-driven review in CI pipelines.

## Volunteer & side projects

- **Paws For A Purpose (Jun 2017–present):** architected and built [parvoalert.com](https://www.parvoalert.com) — fully serverless AWS data collection engine serving thousands of users within free tier; live dashboards for parvovirus researchers across Australia.
- **bridgedoctor.com:** containerised a legacy Ubuntu app, migrated MySQL to IaC-managed Aurora, built the deployment pipeline including full SSL/DNS migration to AWS.
- **Factory automation:** revolutionised a testing facility using Raspberry Pi + Monarco HAT, with a bespoke multi-threaded Python GUI orchestrating the factory's automation.
- **Little Kiwi Bus:** the housebus conversion with Bridget — [littlekiwibus.com](https://www.littlekiwibus.com), blog + [Instagram](https://www.instagram.com/littlekiwibus/) (1,577 followers). Welding, metalwork, roof raise — where the CV's "metalworking" comes from.
- **Reach** (2025–present, personal): accessible gaming platform for disabled people — Unity shell + ~15 game repos, several published, real testers. See `about-me.md`.
- **DEXI** — the DJ career (see `about-me.md`).

## Skills (per CV)

- **Cloud:** AWS, Azure, GCP — architecture, migration, multi-region scale
- **IaC & DevOps:** Terraform, ARM, GitHub Actions, Azure DevOps, GitLab CI, Docker, Kubernetes/EKS
- **Data & AI:** petabyte-scale pipelines, BigQuery, data lakes, ML deployment, AI agent governance (MCP, least-privilege RBAC)
- **Security:** FedRAMP, SOC 2, ISO 27001, GDPR, pipeline security scanning
- **Cost:** FinOps, spend baselines, budget alerting, load testing for unit economics
- **Languages:** Python, Node.js/TypeScript, C#, Bash, PowerShell

## CV notes / possible polish items (Sep 2026)

- CV header says **Arrowtown, New Zealand** — that's the old address from the Bridget years (they lived there until early 2024). She's in Newtown, Wellington now; worth updating for the job hunt.
- All certifications are 2019 or earlier (AWS/GCP certs listed expired 2020–21). The experience clearly outweighs them now, but a current cert or two (or dropping expiry-sensitive framing) may tidy the story for recruiters.
- CV "ALSO" interests: filmmaking, classic cars, metalworking, C# game development in Unity3D, coaching — no mention of Reach by name; could be a strong differentiator for the right employer (real shipped Unity + accessibility work).
