> This repository contains the demonstration code and topic overview for the [DigitalOcean Tech Talk](https://www.digitalocean.com/community/tech_talks/comparing-terraform-and-pulumi) that took place on July 27, 2022.

# Comparing Terraform vs Pulumi

In DevOps, the gold standard for building a deployment platform is using Infrastructure as Code and a GitOps workflow, and there are a couple of popular tools that can enable you and your team to create Infrastructure as Code files. In this talk, Amy will compare and contrast Terraform and Pulumi, she will demonstrate how to create a DigitalOcean Webserver with Terraform and then Pulumi, and finally she will talk through the benefits and drawbacks of each project.

## Pre-requisites

- DigitalOcean Account
- Pulumi Account
- Installed: pulumi
- Installed: pulumi_digitalocean
- Installed: terraform

## GitOps

GitOps is a way of implementing Continuous Deployment for cloud native applications. It focuses on a developer-centric experience when operating infrastructure, by using tools developers are already familiar with, including Git and Continuous Deployment tools.

GitOps opts for building and testing off of the diffs or Merge-Request based deployments. This differs from ‘traditional’ CI/CD models that use a Push-based system.

However, Brian Flanagan of Pulumi discusses that GitOps is less about push-based, declarative systems. "It’s more deciding whether your application tells the environment how to deploy itself, or whether the environment tells your application how to run." The latter being GitOps.

## Infrastructure as Code (IaC)

Infrastructure as Code (IaC) uses two approaches: Declarative and Imperative. A declarative approach defines the desired state of the system, including what resources you need and any properties they should have, and an IaC tool will configure it for you. A declarative approach also keeps a list of the current state of your system objects, which makes taking down the infrastructure simpler to manage. An imperative approach instead defines the specific commands needed to achieve the desired configuration, and those commands then need to be executed in the correct order.

This is just one of the tools that makes GitOps (and good deployment practices in general) work.

## Terraform

Terraform is a Declarative Infrastructure as Code framework.

- Uses Terraform Configuration Files
- Uses proprietary HCL language
- Manually Managed state

## Pulumi

Pulumi uses an Imperative Approach to Infrastructure as Code.

- Uses programming languages such as Go, Python, Java, or Node or uses declarative yaml
- Requires a Pulumi Account
- State is managed by Pulumi’s Dashboard

## Resources

- What is GitOps? https://www.gitops.tech/
- An Inside Look at GitOps https://devops.com/an-inside-look-at-gitops/
- David Flanagan on GitOps: https://twitter.com/rawkode/status/1456169286750375936
- David Flanagan on Pulumi Operator: https://www.pulumi.com/blog/improving-gitops-with-pulumi-operator/
- Declarative vs Imperative approaches to IaC https://www.redhat.com/en/topics/automation/what-is-infrastructure-as-code-iac#benefits-of-iac
- Set up a Production-Ready Droplet https://docs.digitalocean.com/tutorials/recommended-droplet-setup/
- What is Terraform? https://www.terraform.io/intro
- What is Pulumi? https://www.pulumi.com/why-pulumi
