---
domain: devops
task: deployment failure due to registry authentication
dificultad: medium
longitud_objetivo: short
validacion: pipeline succeeds after injecting the secret
---
<!-- markdownlint-disable MD041 -->

Reasoning:

- Apply CoT format and International English (UK) (see «~/rules/rulesets/LINGUISTICS.md» ([../rulesets/LINGUISTICS.md](../rulesets/LINGUISTICS.md)) and flow in «~/rules/rulesets/COMMITTING.md» ([../rulesets/COMMITTING.md](../rulesets/COMMITTING.md))).
- Verify CI/CD prerequisites and registry access secrets.

Steps:

1) Action: review the last failed job in CI.
   Result: 401 error on docker pull from the corporate registry.
2) Action: verify job variables/secrets.
   Result: no REGISTRY_TOKEN variable or configured credentials.
3) Action: define the secret at repository level and reference it in the job.
   Result: REGISTRY_TOKEN defined; job updated to use docker login with the token.
4) Action: retry the pipeline.
   Result: docker pull succeeds and deployment completes.

Conclusion:

- Solution: inject the registry token secret at repository level and authenticate before the pull.
