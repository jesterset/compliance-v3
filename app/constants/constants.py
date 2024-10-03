COMPLIANCE_RULES = {
    "forward_looking_statements": {"expect", "project", "forecast", "estimate", "anticipate", "plan", "will", "predict", "target", "could", "should", "might", "potential", "projected"},
    "insider_information": {"non-public", "confidential", "undisclosed", "insider", "privileged", "secret"},
    "price_target_inquiry": {"price target", "future value", "next quarter", "next year", "expected price", "forecasted price"},
    "mnpi": {"earnings", "revenue", "profit", "loss", "financials", "guidance", "merger", "acquisition", "divestiture", "restructuring", "layoffs", "contracts", "non-public", "confidential", "undisclosed", "not yet announced"},
    "misleading_statements": {"always", "never", "guarantee", "risk-free", "no risk", "promise", "certain", "assured"},
    "over_promising": {"skyrocket", "double", "triple", "explode", "massive gains", "huge returns", "can't lose", "win big"},
    "insider_trading_signals": {"quiet period", "blackout period", "trading window", "no trading", "silent window"},
    "nda_violations": {"NDA", "non-disclosure agreement", "under contract", "binding agreement"},
    "conflict_of_interest": {"conflict of interest", "self-dealing", "personal interest", "undisclosed relationship", "bias", "favoritism"},
    "fiduciary_breach": {"fiduciary duty", "best interest", "confidential duty", "breach of trust", "trustee violation", "mismanagement"},
    "high_risk_language": {"leverage", "high risk", "all in", "bet", "gamble", "penny stocks", "junk bonds", "crypto", "unregulated", "volatile"},
    "unauthorized_disclosures": {"not authorized", "not allowed", "prohibited", "restricted", "off-limits", "forbidden"},
    "investment_advice_without_disclaimer": {"you should invest", "buy now", "sell now", "strong buy", "strong sell", "must buy", "must sell", "this stock will"},
    "regulatory_speculation": {"SEC will", "regulators will", "likely fine", "expect sanctions", "could face penalties", "might be banned", "regulation changes"},
    "legal_violations": {"illegal", "against the law", "prohibited", "unauthorized", "unethical", "fraud", "manipulation", "scam", "tax evasion"},
    "market_manipulation": {"pump and dump", "artificially inflate", "market making", "wash trading", "spoofing", "cornering the market", "price fixing"},
    "unapproved_marketing": {"unapproved", "not vetted", "not reviewed", "draft version", "preliminary version", "for internal use only"}
}

COMPLIANCE_RULES_WITH_PLACEHOLDERS = {
    "forward_looking_statements": [
        "What are {company}'s revenue projections for the {time_period}?",
        "Will {company}'s stock {action} based on {market_conditions} over the {time_period}?",
        "Do you expect {company}'s {sector} performance to outpace competitors in {location} over the {time_period}?",
        "How will {company}'s strategic initiatives impact their earnings event in the {time_period}?",
        "Is {company} likely to adjust its capital allocation strategy given {market_conditions}?"
    ],
    "insider_information": [
        "Is there any {information_type} information about {company}'s upcoming {event}?",
        "Can you share any {insider} insights on {company}'s earnings event for {time_period}?",
        "What {confidentiality} details can you provide about {company}'s {document} and its impact on their stock price?",
        "Is there any {confidentiality} information about {company}'s {merger_acquisition} announcement?",
        "Do you have access to any {insider} reports about {company}'s {contracts} or agreements?"
    ],
    "price_target_inquiry": [
        "What's your price target for {company}'s stock over {time_period}?",
        "Do you see {company}'s stock reaching {price} given {market_conditions}?",
        "What are the expected {sector} returns for {company} by {time_period}?",
        "Could {company}'s stock hit {price} in the {time_period}?",
        "What valuation do you anticipate for {company} based on {market_conditions} and {sector} trends?"
    ],
    "mnpi": [
        "Is there any {insider} data on {company}'s earnings event before its public release?",
        "Do you have {confidentiality} info on {company}'s {merger_acquisition}?",
        "Can you provide any {information_type} insights on {company}'s project?",
        "Are there any material non-public details regarding {company}'s earnings event?",
        "Can you disclose {company}'s {document} under {insider} access?"
    ],
    "misleading_statements": [
        "{company}'s stock is guaranteed to {action} over the {time_period}.",
        "This trade has {no_risk}; {company} is a sure bet.",
        "I {promise} {company}'s stock will hit {price} in {time_period}.",
        "There's {no_downside} to investing in {company} right now.",
        "Investing in {company} is a {risk_free} opportunity."
    ],
    "over_promising": [
        "Expect {high_return} from {company} in the {time_period}.",
        "{company} is set to {action} over the next {time_period}.",
        "You can't lose with {company}; the stock is poised to {action}.",
        "{company} will {action} in the {time_period}—the market is aligned perfectly.",
        "This is the perfect moment to get in on {company}'s {event} before they {action}."
    ],
    "insider_trading_signals": [
        "Are we in a blackout period for {company}'s stock?",
        "Is it permissible to trade {company}'s stock during this quiet period?",
        "When does the blackout period end for {company}?",
        "Can we execute trades on {company} now, or are we restricted?",
        "Is the trading window currently closed for {company}?"
    ],
    "nda_violations": [
        "Are we allowed to disclose {company}'s {document} under the NDA?",
        "Does the NDA cover {company}'s project, or can we discuss it?",
        "Is this {document} related to {company} covered under the NDA?",
        "Are there restrictions on sharing {company}'s {contracts} with external parties?",
        "Can we talk about {company}'s project, or is it protected by NDA?"
    ],
    "conflict_of_interest": [
        "Do you have any personal interest in this {merger_acquisition} involving {company}?",
        "Is there any conflict of interest with {company}'s deal that needs disclosure?",
        "Does {company}'s project pose any potential conflict of interest?",
        "Are there any undisclosed relationships that could affect {company}'s transaction?",
        "Is there a risk of bias in {company}'s {event} due to a conflict of interest?"
    ],
    "fiduciary_breach": [
        "Has {company}'s trustee breached their fiduciary duty?",
        "Is {company} involved in a breach of fiduciary trust with this project?",
        "Could {company} face legal action for fiduciary mismanagement?",
        "Is there evidence that {company} has violated fiduciary obligations?",
        "Do you believe {company}'s actions are a breach of fiduciary duty?"
    ],
    "high_risk_language": [
        "{company}'s stock is highly volatile but could provide {high_return}.",
        "If you're willing to take a chance, {company}'s stock could {action}.",
        "{company} is a high-risk, high-reward play given {market_conditions}.",
        "This is a speculative investment on {company}, but the upside is massive.",
        "Investing in {company} comes with high risk language, but the potential rewards are great."
    ],
    "unauthorized_disclosures": [
        "Are we authorized to share {company}'s {document} externally?",
        "Can we disclose {company}'s {document}, or is it restricted?",
        "Is {company}'s {event} considered confidential, or can we discuss it?",
        "Are we allowed to distribute {company}'s {document} before it's official?",
        "Is {company}'s {document} ready for public release, or is it still restricted?"
    ],
    "investment_advice_without_disclaimer": [
        "I strongly advise buying {company}'s stock now.",
        "You should invest in {company}'s stock before the {event} is announced.",
        "Sell {company}'s stock before {market_conditions} change.",
        "Increase your position in {company}'s stock; {high_return} is expected.",
        "This is a {risk_free} opportunity to invest in {company}."
    ],
    "regulatory_speculation": [
        "Will {company} face regulatory penalties from the {regulatory_body}?",
        "Do you expect {company} to be fined by the {regulatory_body} due to activity?",
        "Could the {regulatory_body} launch an investigation into {company}?",
        "Is there a chance {company}'s actions could result in sanctions by the {regulatory_body}?",
        "Do you think {company} will face enforcement action from the {regulatory_body}?"
    ],
    "legal_violations": [
        "Is {company}'s activity illegal under current regulations?",
        "Could {company} be involved in legal violations related to their project?",
        "Do you think {company}'s {action} could be considered unlawful?",
        "Could {company} face litigation due to activity in the {sector}?",
        "Is there any risk of legal action against {company} for activity?"
    ],
    "market_manipulation": [
        "Is {company} involved in any market manipulation tactics like spoofing?",
        "Do you think the recent activity in {company}'s stock is a pump-and-dump?",
        "Is {company} engaging in price manipulation, or is this just market movement?",
        "Could {company}'s actions be considered wash trading or market manipulation?",
        "Is there concern that {company} is influencing the market in the {sector}?"
    ],
    "unapproved_marketing": [
        "Has {company}'s marketing campaign been approved for release?",
        "Are we allowed to distribute {company}'s advertisement, or is it unapproved?",
        "Is {company}'s marketing material ready for public view?",
        "Can we release {company}'s marketing campaign, or does it need more vetting?",
        "Is this an unapproved draft of {company}'s campaign?"
    ],
    "weather": [
        "How will weather in {location} affect {company}'s {event}?",
        "Does {company}'s stock depend on weather patterns in {location}?",
        "Will {location}'s hurricane season impact {company}'s {sector} performance?",
        "How does extreme weather in {country} affect {company}'s supply chain?",
        "Will weather changes in {country} affect {company}'s stock?"
    ],
    "general": [
        "What are {company}'s key products?",
        "How does {company}'s leadership affect stock performance?",
        "How has {company}'s growth strategy evolved over the past {years} years?",
        "What is {company}'s position in the {sector} market?",
        "What impact will {company}'s new product launch have on the {sector} market?"
    ]
}