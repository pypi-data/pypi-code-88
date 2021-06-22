from itertools import zip_longest
import re
from collections import defaultdict
from uuid import UUID

from pyfactcast.app.business.entities import CollectSpec
from pyfactcast.client.entities import Fact, SubscriptionSpec, VersionedType
from typing import Dict, Iterable, List
from pyfactcast.client.sync import FactStore


def _filter_types(*, fs: FactStore, namespace: str, it: Iterable[str]) -> Iterable[str]:
    if not it:
        return it

    types_for_namespace = fs.enumerate_types(namespace=namespace)
    res = set()

    # TODO: Make the regex stuff beautiful
    regexes = [re.compile(elem) for elem in it]
    for regexp in regexes:
        res.update(list(filter(regexp.fullmatch, types_for_namespace)))

    return res


def subscribe(
    namespace: str,
    follow: bool,
    from_now: bool = False,
    after_fact: UUID = None,
    fact_types: List[str] = [],  # noqa: B006 this is not written to
    type_versions: List[int] = [],  # noqa: B006 this is not written to
    *,
    fact_store: FactStore = FactStore(),
) -> Iterable[Fact]:

    if len(type_versions) > len(fact_types):
        raise ValueError(
            (
                "More versions than event types given."
                "Please provide the same number of types and versions or more types than versions."
            )
        )

    if type_versions:
        lookup_types = [
            SubscriptionSpec(
                ns=namespace, type=VersionedType(name=type_name, version=version)
            )
            for type_name, version in zip_longest(
                fact_types, type_versions, fillvalue=0
            )
        ]

    with fact_store as fs:

        if not type_versions:
            resolved_types = _filter_types(fs=fs, namespace=namespace, it=fact_types)
            lookup_types = [
                SubscriptionSpec(
                    ns=namespace, type=VersionedType(name=type_name, version=version)
                )
                for type_name, version in zip_longest(
                    resolved_types, type_versions, fillvalue=0
                )
            ]

        if not fact_types:
            lookup_types = [SubscriptionSpec(ns=namespace)]

        return fs.subscribe(
            subscription_specs=lookup_types,
            continuous=follow,
            from_now=from_now,
            after_fact=after_fact,
        )


def collect(
    collect_specs: List[CollectSpec], *, fact_store: FactStore = FactStore()
) -> Iterable[Fact]:

    subscription_specs = [
        SubscriptionSpec(
            ns=collect_spec.ns,
            type=VersionedType(name=collect_spec.type, version=collect_spec.version),
        )
        for collect_spec in collect_specs
    ]

    with fact_store as fs:
        return fs.subscribe(subscription_specs=subscription_specs)


def collect_by_namespace(
    collect_specs: List[CollectSpec], *, fact_store: FactStore = FactStore()
) -> Dict[str, Iterable[Fact]]:

    spec_by_namespace = defaultdict(lambda: [])
    for spec in collect_specs:
        spec_by_namespace[spec.ns].append(spec)

    result = {}
    with fact_store as fs:
        for ns, specs in spec_by_namespace.items():
            subscription = collect(
                collect_specs=specs, fact_store=fs
            )  # IMPR: use Async client once available
            result[ns] = subscription

    return result
