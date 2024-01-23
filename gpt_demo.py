from openai import OpenAI

client = OpenAI() # TODO: replace with huggingface API
# https://platform.openai.com/docs/quickstart?context=python
# https://platform.openai.com/api-keys
# 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
# export OPENAI_API_KEY='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' # TODO: add your own key...

# OpenAI platform: https://platform.openai.com/


print("Hello, what is the objective of your ISO form today")
# TODO: get user input
objective_input = "I want to create an ISO for bottling wine!"


print("Can you give me a couple comma separated keywords for your project?")
# TODO: maybe have this as a lookup? (preset keywords)
# mandatory that they choose at least one.
keyward_input = "wine,bottling,finland,uruguay,sanitize,GAI machine"


print(
    "Thanks! Which market are you targetting? (important for the ISO regulations). Also any specific requirements for your clients would be helpful to supply!"
)
# TODO: get user input
market_input = (
    "I want to target the Uruguayan wine market (with overseas export to Finland)"
    + " We are hoping to work in the beverage market, our clients in Finland require calorie & alcohol content labels"
    + " Our clients in Uruguay require warning of +18 consumption"
)  #  TODO: get this from user.

print(
    "What resources do you have (machines, materials, consumables)? Can you give me a rough description of procedures / activities which you already employ?"
)  #
# TODO: get user input
resources_procedure_input = (
    "I have a GAI machine. I have synthetic & non-synthetic bottle caps. I have 750 mL wine bottles."
    + " Roughly we currently, clean the machine, sanitize the bottles with steam?, we push through 100 liters of wine "
    + " to prepare the pipes..., pack the bottles once we finish the bottling line. "
)  #  TODO: get this from user.


print("What procedures (if any) do you currently employ for quality control?")
# TODO: have user input the quality_control_input
quality_control_input = (
    "Currently we do random quality control on 1 bottle out of every 200, testing for if the bottle is correctly filled (to the right level) "
    + "And if the labels are adhered correctly, not ripped. If there are bacteria growing in there..."
)

example_isos = []
for keyword in keyward_input.split(","):
    # TODO: implement get_iso_examples()
    example_iso = get_iso_examples(key_input=keyword)
    example_iso.append(example_iso)

    # TODO: IF no keywords, randomly choose a couple of ISO forms

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            # "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair.",
            "content": "You are a ISO standard expert, skilled in creating procedures also filling out forms (in spanish) for managing non-conformities, recalls, and complaints.",
        },
        {
            "role": "system",
            "content": "This is the objective of the user: " + objective_input,
        },
        {
            "role": "system",
            "content": "This is the target market of the user: " + market_input,
        },
        {
            "role": "system",
            "content": "This is the resource / procedure  of the user: "
            + resources_procedure_input,
        },
        {
            "role": "system",
            "content": "This is the quality control procedures  of the user: "
            + quality_control_input,
        },
        {
            "role": "user",
            "content": (
                "Can you build me a ISO standard form with the information above? "
                + " Here are some relevant example ISO forms for similar processes: "
                + [example for example in example_isos]
            ),
        },
    ],
)

print(completion.choices[0].message)
