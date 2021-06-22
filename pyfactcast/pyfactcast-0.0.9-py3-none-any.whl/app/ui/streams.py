from pathlib import Path
from typing import Iterable, List, Optional
from uuid import UUID
from pydantic import parse_file_as
import typer
from rich.console import Console
from rich.table import Table
from datetime import datetime
import json
from pyfactcast.app.business.entities import CollectSpec

import pyfactcast.app.business.streams as business

app = typer.Typer()
console = Console()


def print_iterable_as_json_list(iterable: Iterable) -> None:
    console.print("[")
    try:
        it = iter(iterable)

        last = next(it)  # type: ignore
        console.print(f"{last.json(indent=2)}", soft_wrap=True)

        for elem in it:
            last = elem
            console.print(f",{last.json(indent=2)}", soft_wrap=True)
    except StopIteration:
        return
    finally:
        console.print("]")


def write_iterable_as_json_list(iterable: Iterable, out: Path) -> None:
    with open(out, "w") as f:
        f.write("[")
        try:
            it = iter(iterable)

            last = next(it)  # type: ignore
            f.write(f"{last.json(indent=2)}")

            for elem in it:
                last = elem
                f.write(f",{last.json(indent=2)}")
        except StopIteration:
            return
        finally:
            f.write("]")


@app.command()
def subscribe(
    ctx: typer.Context,
    namespace: str,
    follow: bool = typer.Option(
        False, "--follow", help="Stay connected and listen for new events."
    ),
    from_now: bool = typer.Option(
        False, "--from-now", help="Follow the event stream starting now."
    ),
    after_fact: UUID = typer.Option(
        None, help="Get all events in the stream that happened after a certain ID."
    ),
    json_format: bool = typer.Option(False, "--json", help="Output raw json events."),
    fact_types: List[str] = typer.Option(
        [],
        "--type",
        help="The types of events to get. Can be used multiple times. Supports regexp.",
    ),
    type_versions: List[int] = typer.Option(
        [],
        "--version",
        help="The versions of the types to get. Will be right padded with latest. If used regex for types is not supported.",
    ),
) -> None:
    """
    Subscribe to an eventstream.

    You can select types you want to subscribe to. When doing so you can also use regexes to subscribe to multiple
    event types in short order for example ``... subscribe machinery --type Assembly.*``
    will get you all Assembly events for example AssemblyCreated, AssemblyCompleted, AssemblyDestroyed but nothing related
    to Subassemblies. If you specify no types, all types will be streamed.

    You can also get event types in specific versions.
    You can either specify them intermixed with the types like this
    ``... subscribe machinery --type AssemblyCreated --version 1 --type AssemblyUsed --version 3``
    or you can write them out after each other like this
    ``... subscribe machinery --type AssemblyCreated --type AssemblyUsed --version 1 --version 3``.
    In both cases you will get version 1 of AssemblyCreated and version 3 of AssemblyUsed.
    You can specify fewer versions than types. In this case matching will be left to right by postion in the list.
    Types without a version will give you the latest version. This leads to a slightly strange case where
    ``... subscribe machinery --type AssemblyCreated --type AssemblyUsed --version 2``
    will give you version 2 of AssemblyCreated and the latest version of AssemblyUsed.
    It is recommended to put the types you need the latest version of last and use intermixed notation before that.
    If you want to explicitly specify the latest version, please specify ``--version 0``


    To keep other complexities out of this, if you use versions you will not be able
    to use regexes. This is mostly due to the ambiguities that come along when you specify something like this
    ``... subscribe machinery --type Assembly.* --version 2`` do you want version 2 of everything or version 2 of the first match
    and latest of everything else?

    If you are looking for information on ``tee`` and ``--follow`` please check the
    :ref:`Streams FAQ<faq/streams:Fact Stream FAQ>`.
    """
    subscription = business.subscribe(
        namespace=namespace,
        follow=follow,
        after_fact=after_fact,
        from_now=from_now,
        fact_types=fact_types,
        type_versions=type_versions,
        fact_store=ctx.obj["fact_store"],
    )

    if json_format:
        print_iterable_as_json_list(subscription)
        return

    for elem in subscription:
        table = Table(show_header=False, show_lines=True, header_style="bold magenta")
        table.add_column("Time")
        table.add_column("Type")
        table.add_column("Header")
        table.add_column("Payload")
        table.add_row(
            datetime.fromtimestamp(int(elem.header.meta["_ts"][:10])).isoformat(),  # type: ignore
            elem.header.type,
            elem.header.json(indent=2),
            json.dumps(elem.payload, indent=2),
        )
        console.print(table)


@app.command()
def collect(
    ctx: typer.Context,
    collect_spec: Path,
    out: Optional[Path] = typer.Option(
        None, help="The output file or folder to which the result is to be delivered."
    ),
    by_namespace: bool = typer.Option(
        False,
        "--by-namespace",
        help='If set the result will be output to one file per namespace. Requires "out" option to be a directory.',
    ),
) -> None:
    """
    This command helps in piecing together more complex scenarios. It takes a file containing
    a list of dicts ``[{"ns": "testNamespace", "type": "testType", "version":2}]`` where ``version``
    is optional. The type is not regexp-able. This can be used to gather the base data for projections
    which can assist in debugging.

    The command will collect all events matching the specification into one event stream and either
    print it to screen of output it to a file.
    If you need the eventstreams separated by namespace you MUST pass an output directroy along
    with the ``--by--namespace`` option. The resulting eventstreams will be stored as json lists
    in that directory in files named after the namespaces.
    """
    collect_specs = parse_file_as(List[CollectSpec], collect_spec)
    fs = ctx.obj["fact_store"]

    if by_namespace:
        if not out:
            console.print(
                "--by-namespace is set. Please provide a directory through --out.",
                style="red",
            )
            raise typer.Exit(1)
        if not out.is_dir():
            console.print(
                "--by-namespace is set. --out must be a directory.", style="red"
            )
            raise typer.Exit(1)

        namespaced_results = business.collect_by_namespace(
            collect_specs=collect_specs, fact_store=fs
        )
        for ns, result in namespaced_results.items():
            write_iterable_as_json_list(result, out.joinpath(f"{ns}.json"))

    subscription = business.collect(collect_specs=collect_specs, fact_store=fs)

    if not out:
        print_iterable_as_json_list(subscription)

    if out and not by_namespace:
        write_iterable_as_json_list(subscription, out)
