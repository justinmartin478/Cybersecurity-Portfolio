# Docker, Kubernetes, GitHub, and Slack

*What each product does, who makes it, how it is deployed, and how it supports software development and SaaS delivery*

**Course:** IT295 CompTIA Project+ Cert Prep &nbsp;·&nbsp; **Module:** 1 &nbsp;·&nbsp; **Type:** Report

> The full assignment is rendered below. The original and a formal copy are available for download: [**Word document**](./IT295_Module_1_Research_Project_Portfolio_Justin_Martin.docx) · [**PDF**](./IT295_Module_1_Research_Project_Portfolio_Justin_Martin.pdf)

| Team Member | Course | Assignment | Date |
| --- | --- | --- | --- |
| Justin Martin | IT 295 | Module 1 Research | September 23, 2026 |

---

*This report compares four products used in modern software development and collaboration, with emphasis on purpose, producer, deployment model, cloud use, and support for software development or SaaS delivery.*

## At a Glance

| Product | Producer | Type | Requires the cloud? | Dev / SaaS role |
| --- | --- | --- | --- | --- |
| Docker | Docker, Inc. | Container platform | No. Local, on premises, cloud, or hybrid | Packages apps for consistent build, test, and deploy |
| Kubernetes | CNCF community, originally Google | Container orchestration | No. On premises, cloud, hybrid, or managed | Deploys, scales, and heals containerized apps |
| GitHub | GitHub, a Microsoft company | Code hosting and CI/CD | GitHub.com yes. Enterprise Server can be self-hosted | Source control, code review, Actions CI/CD |
| Slack | Slack Technologies, a Salesforce company | Team communication | Yes. Slack-hosted SaaS only | Team coordination, integrations, custom apps |

## 01. Docker

*Container Platform*

| Producer | Requires Cloud | Runs in Cloud |
| --- | --- | --- |
| Docker, Inc. | No | Yes |

**Q1. What does the product do?**

Docker is a container platform used to develop, package, ship, and run applications. Instead of depending on the exact software installed on a host computer, an application can be packaged into a container with the runtime and dependencies it needs. This makes the application more consistent when it moves between development, testing, and production environments.

**Q2. Who produces it?**

Docker is produced by Docker, Inc. Docker also maintains Docker Desktop and other commercial tools and services around the Docker ecosystem. The core Docker Engine is open source and is built on the Moby project, so the community contributes to it as well.

**Q3. How is it structured and deployed? Does it require the cloud?**

Docker uses container images as portable application packages and containers as running instances of those images. Docker Engine can run on local or remote hosts, while Docker Desktop provides a developer-focused environment for desktop systems. **Docker does not require a public cloud to operate.** Containers can run on a developer's computer, in an on-premises data center, with a cloud provider, or in a hybrid environment.

**Q4. Does it facilitate software development or SaaS delivery?**

Yes. Software development is one of Docker's primary uses. Developers can build an application in a standardized container, test the same image, and then deploy it into production. This consistency makes Docker useful in continuous integration and continuous delivery (CI/CD) pipelines. It can also package the components of a SaaS application so they can be deployed repeatedly across development and production environments.

#### External References

- Docker Docs, "What is Docker?": <https://docs.docker.com/get-started/docker-overview/>
- Docker, "Contact Docker": <https://www.docker.com/company/contact/>

## 02. Kubernetes

*Container Orchestration*

| Producer | Requires Cloud | Runs in Cloud |
| --- | --- | --- |
| CNCF open-source community (created by Google) | No | Yes |

**Q1. What does the product do?**

Kubernetes, commonly shortened to K8s, is an open-source platform for orchestrating containerized applications. It manages workloads across a cluster and can automate tasks such as deployment, scaling, load balancing, recovery from failures, and application updates. In simple terms, Docker can package and run containers, while Kubernetes is designed to coordinate large groups of containers and keep applications running in their desired state.

**Q2. Who produces it?**

Kubernetes was originally created by Google and released as an open-source project in 2014. The project is now hosted by the Cloud Native Computing Foundation (CNCF) and developed by a broad open-source community rather than being a proprietary product produced by one company.

**Q3. How is it structured and deployed? Does it require the cloud?**

A Kubernetes cluster is built around a control plane and one or more worker nodes. The control plane manages the cluster, while worker nodes run application workloads inside Pods. Each node uses a container runtime such as containerd or CRI-O, and images built with Docker run on Kubernetes without changes. **Kubernetes does not require a public cloud.** A cluster can run on premises, in a public cloud, or in a hybrid environment. Managed Kubernetes services are also offered by major cloud providers.

**Q4. Does it facilitate software development or SaaS delivery?**

Yes. Kubernetes is heavily used for deploying and operating software after it has been containerized. It supports automated rollouts and rollbacks, scaling, self-healing, service discovery, configuration management, and other capabilities useful for production applications. These features make Kubernetes well suited to operating cloud-native applications and SaaS platforms that need reliability and the ability to scale.

#### External References

- Kubernetes Documentation, "Overview": <https://kubernetes.io/docs/concepts/overview/>
- Kubernetes Documentation, "Cluster Architecture": <https://kubernetes.io/docs/concepts/architecture/>
- CNCF, Kubernetes project history: <https://www.cncf.io/announcements/2018/08/29/cncf-receives-9-million-cloud-credit-grant-from-google/>

## 03. GitHub

*Code Hosting and CI/CD*

| Producer | Requires Cloud | Runs in Cloud |
| --- | --- | --- |
| GitHub (Microsoft) | Only for GitHub.com | Yes |

**Q1. What does the product do?**

GitHub is a developer platform centered on Git repositories. It allows developers and teams to store source code, track changes, create branches, review pull requests, manage issues, document projects, and collaborate on software. A repository can serve as the central location for a project's code and development history.

**Q2. Who produces it?**

GitHub is produced and operated by GitHub. GitHub became part of Microsoft after Microsoft's acquisition of the company in 2018, while GitHub continues to operate as its own developer platform and brand.

**Q3. How is it structured and deployed? Does it require the cloud?**

GitHub.com is primarily delivered as a cloud hosted service, so normal use of the website and hosted repositories depends on GitHub's online infrastructure. GitHub Enterprise also offers two deployment options: GitHub Enterprise Cloud, which GitHub hosts, and GitHub Enterprise Server, which an organization can operate on premises or through a supported public cloud provider. Developers can still clone repositories and work with Git locally while disconnected, then synchronize their changes later. GitHub Actions can also use GitHub hosted or self hosted runners.

**Q4. Does it facilitate software development or SaaS delivery?**

Yes. GitHub directly facilitates software development throughout the software lifecycle. Beyond source control and collaboration, GitHub Actions provides CI/CD automation that can build, test, and deploy code when repository events occur. Teams can therefore use GitHub to manage source code and automate steps that move software from development toward production and SaaS delivery. GitHub.com is also a SaaS product itself, so it is an example of software delivered as a service as well as a tool for building it.

#### External References

- GitHub, "About GitHub": <https://github.com/about>
- GitHub Docs, "Understanding GitHub Actions": <https://docs.github.com/en/actions/get-started/understand-github-actions>
- GitHub Docs, "GitHub's plans": <https://docs.github.com/en/get-started/learning-about-github/githubs-plans>
- Microsoft, "Microsoft to acquire GitHub": <https://news.microsoft.com/source/2018/06/04/microsoft-to-acquire-github-for-7-5-billion/>

## 04. Slack

*Team Communication*

| Producer | Requires Cloud | Runs in Cloud |
| --- | --- | --- |
| Slack Technologies (Salesforce) | Yes | Yes, SaaS only |

**Q1. What does the product do?**

Slack is a collaboration and business communication platform organized around workspaces, channels, direct messages, files, calls, applications, and automated workflows. Teams use it to keep conversations and project information in shared spaces instead of relying only on email. Slack can also connect to external services so notifications and actions from other tools appear inside a team's workspace.

**Q2. Who produces it?**

Slack was developed by Slack Technologies. Salesforce completed its acquisition of Slack Technologies in 2021, so Slack is now part of Salesforce while continuing to operate under the Slack brand.

**Q3. How is it structured and deployed? Does it require the cloud?**

Slack is a cloud-delivered service. Users access Slack through desktop, mobile, and web clients that connect to Slack's hosted platform. Unlike Docker or Kubernetes, there is no version of the core Slack service that an organization installs on its own servers, **so Slack does require the cloud to operate.** For custom development, however, Slack supports both Slack-hosted workflows and self-hosted applications built with frameworks such as Bolt.

**Q4. Does it facilitate software development or SaaS delivery?**

Yes, although Slack's role is different from Docker, Kubernetes, or GitHub. Slack facilitates development mainly through team communication, integrations, automation, APIs, and custom apps. Development teams can connect tools to Slack to receive alerts, coordinate work, and automate workflows. Slack's developer platform also lets programmers build applications and custom workflow steps using APIs, SDKs, and frameworks such as Bolt for Python, JavaScript, and Java. Slack itself is also a SaaS product, which makes it a direct example of software delivered as a service.

#### External References

- Slack Developer Docs, "Slack platform overview": <https://docs.slack.dev/concepts/overview/>
- Slack Developer Docs, "Workflows": <https://docs.slack.dev/workflows/>
- Salesforce, "Salesforce Completes Acquisition of Slack": <https://www.salesforce.com/news/press-releases/2021/07/21/salesforce-slack-deal-close/>

## References

Cloud Native Computing Foundation. (2018, August 29). *CNCF receives $9 million cloud credit grant from Google.* https://www.cncf.io/announcements/2018/08/29/cncf-receives-9-million-cloud-credit-grant-from-google/

Docker. (n.d.-a). *Contact Docker.* Docker, Inc. https://www.docker.com/company/contact/

Docker. (n.d.-b). *What is Docker?* Docker Docs. https://docs.docker.com/get-started/docker-overview/

GitHub. (n.d.-a). *About GitHub.* https://github.com/about

GitHub. (n.d.-b). *GitHub's plans.* GitHub Docs. https://docs.github.com/en/get-started/learning-about-github/githubs-plans

GitHub. (n.d.-c). *Understanding GitHub Actions.* GitHub Docs. https://docs.github.com/en/actions/get-started/understand-github-actions

Kubernetes. (n.d.-a). *Cluster architecture.* Kubernetes Documentation. https://kubernetes.io/docs/concepts/architecture/

Kubernetes. (n.d.-b). *Overview.* Kubernetes Documentation. https://kubernetes.io/docs/concepts/overview/

Microsoft. (2018, June 4). *Microsoft to acquire GitHub for $7.5 billion.* Microsoft News. https://news.microsoft.com/source/2018/06/04/microsoft-to-acquire-github-for-7-5-billion/

Salesforce. (2021, July 21). *Salesforce completes acquisition of Slack.* https://www.salesforce.com/news/press-releases/2021/07/21/salesforce-slack-deal-close/

Slack. (n.d.-a). *Slack platform overview.* Slack Developer Docs. https://docs.slack.dev/concepts/overview/

Slack. (n.d.-b). *Workflows.* Slack Developer Docs. https://docs.slack.dev/workflows/

## Outcome

I researched Docker, Kubernetes, GitHub, and Slack and answered the same four questions for each product. I compared who produces each one, how it is deployed, and whether it needs the cloud. I also explained how each tool supports software development and SaaS delivery, from packaging and orchestration to source control and team communication.
