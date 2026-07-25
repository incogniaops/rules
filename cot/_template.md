---
domain: devops
task: deployment failure diagnosis
dificultad: medium
longitud_objetivo: short
validacion: command output matches expected state
---
<!-- markdownlint-disable MD041 -->

Reasoning:
- Identify the failure point in the deployment pipeline.
- Verify prerequisites and dependencies in logical order.
- Style and flow references: «~/rules/rulesets/LINGUISTICS.md» ([../rulesets/LINGUISTICS.md](../rulesets/LINGUISTICS.md)), «~/rules/rulesets/COMMITTING.md» ([../rulesets/COMMITTING.md](../rulesets/COMMITTING.md)) and «~/rules/README.md» ([../README.md](../README.md)).

Steps:
1) Action: review CI logs for the last failed job.
   Result: authentication error when accessing the container registry.
2) Action: verify the access token environment variable.
   Result: variable not defined in the runner environment.
3) Action: consult internal documentation for secret provisioning.
   Result: the secret must be injected at repository level.

Conclusion:
- Solution: define the token as a repository secret and reference it in the job; retry the pipeline.
