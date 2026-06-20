# Resolver
**An agent that knows when not to act, and can prove why.**

## The Refusal-Gate

A customer asks for a refund. Using a deterministic policy gate (not model vibes), the agent first *flags the account* and then *correctly* refuses with a structured and inspectable audit record explaining the decision.

The biggest risk for a business implementing a resolver is that their agent starts refunding any individual (regardless if they are a customer or not), quickly creating a legal and financial mess. This is why I prioritized this gate for the first implementation of the resolver-mcp. The important aspect of the resolver which is exemplified in this gate is that the decision is deterministic, not a decision that an LLM makes.