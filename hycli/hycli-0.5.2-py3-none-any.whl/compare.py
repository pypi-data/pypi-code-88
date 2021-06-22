import click
from halo import Halo
from hycli.commons.excel_adapter import ExcelAdapter
from hycli.commons import calculate_improvements as improvements


@click.command(context_settings=dict(max_content_width=200))
@click.argument("file_path_1", type=click.Path(exists=True))
@click.argument("file_path_2", type=click.Path(exists=True))
@click.option(
    "-o",
    "--output",
    help="output path for xlsx file relative from current location (ends with .xlsx)",
)
@click.option(
    "-t",
    "--truth",
    help="ground truth path. For performing three way comparison",
    default=None,
)
@click.pass_context
def compare(ctx, file_path_1, file_path_2, output=None, truth=None):
    """ compares extraction data between two excel files """
    spinner = Halo(spinner="dots")
    spinner.start()

    def _evaluate_models():
        """Performs 3- way comparison. Evaluates which model performs better."""
        spinner.start("Starting evaluation..\n")

        ea_1 = ExcelAdapter(truth, file_path_1)
        ea_2 = ExcelAdapter(truth, file_path_2)

        comparisons_1 = ea_1.compare()
        comparisons_2 = ea_2.compare()

        evaluation_of_improvements = improvements.calculate_improvements(
            comparison_1=comparisons_1, comparison_2=comparisons_2
        )
        evaluation_of_improvements.to_excel(output, sheet_name="header_evaluation")

        spinner.succeed(f"Please check evaluation here: {output} \n")

    def _compare_models():
        """ Performs comparison between two datasets"""

        spinner.start("Starting comparison..\n")
        ea = ExcelAdapter(file_path_1, file_path_2)
        comparisons = ea.compare()
        ea.export_comparison_to_excel(comparisons, output)
        spinner.succeed(f"Please check comparison here: {output} \n")

    if truth:
        output = "evaluation.xlsx" if output is None else output
        _evaluate_models()
    else:
        output = "comparison.xlsx" if output is None else output
        _compare_models()
