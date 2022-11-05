#!/usr/bin/env python
# coding: utf-8
__author__ = "Sarthak Shah"
__version__ = "1.0.1"
__maintainer__ = "Sarthak Shah"
__email__ = "er.sarthak@outlook.com"
__status__ = "Production"

"""Features
Aggregates and applications — base classes for event-sourced aggregates and applications. Suggests how to structure an event-sourced application. All classes are fully type-hinted to guide developers in using the library.

Worked examples — includes examples showing how to develop aggregates, applications and systems.

Extensions
The GitHub organisation Event Sourcing in Python hosts extension projects for the Python eventsourcing library.
 There are projects that adapt popular ORMs such as Django and SQLAlchemy. There are projects that adapt specialist event stores
  such as Axon Server, EventStoreDB. There are projects that support popular NoSQL databases such as DynamoDB and MongoDB. There are also projects that provide examples of using the library with web frameworks as FastAPI and Flask. And there are examples of event-sourced applications and systems of event-sourced applications, such as the Paxos system, which is used as the basis for a replicated state machine, which is used as the basis for a distributed key-value store.
"""

from eventsourcing.domain import Aggregate, event
from unittest import TestCase


class Elephant(Aggregate):

    @event("Elephant instance created!!")
    def __init__(self, name):
        self.name = name
        self.attributes = []

    @event("new elephant attribute added!")
    def add_attributes(self, new_attr):
        self.attributes.append(new_attr)


class Test(TestCase):
    def test_event_records(self):
        ramesh = Elephant("The Ultimate Ramesh")
        ramesh.add_attributes("roll over")
        ramesh.add_attributes("trunk shower")

        events = ramesh.collect_events()

        # print(type(events))
        # for i in events:
        #     print(i)

        copy = None
        for e in events:
            copy = e.mutate(copy)

        # print(type(copy), dir(copy), sep="\n")
        print(copy.attributes)
        self.assertEqual(copy.attributes, ["roll over", "trunk shower"])