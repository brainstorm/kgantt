kgantt
======

Overview:
========

An attempt to draw Gantt charts using Trello and Google charts API.

![alt text](https://raw.github.com/brainstorm/kgantt/master/gantt.png "Project management ruins lifes")

At the moment this system requires:

1. Manually set deadlines to all cards (tasks) that one wants to see in the gantt chart.
2. [TODO] Manually specified dependencies via the checklist system (keyword: "Depends on" and a link or card id).
3. That you re-run the script to update the view of the updated gantt chart (every day? every board meeting?).

Installation:
============

At the moment, write two files in the same folder you are running the script from: .fuser and .fpasswd

They should contain the foauth.org user and password, respectively. One should have activated the Trello foauth.org
binding though:

https://foauth.org/services/#trello-modal

In essence foauth allows the developer to bypass the OAuth hassle by having a plain old HTTP Basic authentication
instead of all the API key/token business.

TODO:
====

* Restructure the proof of concept in proper entities/classes.
* See future thoughs in the code itself: https://github.com/brainstorm/kgantt/blob/master/kgantt.py#L42
