#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import logging
from sanji.core import Sanji
from sanji.core import Route
from sanji.connection.mqtt import Mqtt


class Hellosanji(Sanji):

    def init(self, *args, **kwargs):
        self.message = "Hello Sanji!"

    @Route(methods="get", resource="/hellosanji")
    def get(self, message, response):
        return response(data={"message": self.message})

    @Route(methods=["post", "put"], resource="/hellosanji")
    def put(self, message, response):
        self.message = message.data["message"]
        return response(data=self.message)

    @Route(methods="delete", resource="/hellosanji")
    def delete(self, message, response):
        self.message = ""
        return response(data=self.message)


if __name__ == "__main__":
    FORMAT = "%(asctime)s - %(levelname)s - %(lineno)s - %(message)s"
    logging.basicConfig(level=0, format=FORMAT)
    logger = logging.getLogger("Hellosanji")

    hellosanji = Hellosanji(connection=Mqtt())
    hellosanji.start()
