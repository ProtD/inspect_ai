from inspect_ai import Task, task
from inspect_ai.dataset import Sample
from inspect_ai.scorer import includes
from inspect_ai.solver import generate
from inspect_ai.solver._use_tools import use_tools
from inspect_ai.tool import web_browser_tools


@task
def browser():
    return Task(
        dataset=[
            Sample(
                input="Use the web browser tool to navigate to https://www.gov.uk/government/organisations/ai-safety-institute. Then, use the search input on that page to search for 'ai safety'. Report the links that you find in the search results."
            )
        ],
        solver=[
            use_tools(web_browser_tools()),
            generate(),
        ],
        scorer=includes(),
        sandbox="docker",
    )
