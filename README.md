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

At the moment, write two files: .key and .token

They should contain the trello api developer key and token, respectively. Those can be found at:

https://trello.com/1/appKey/generate#

In the future that should not be necessary if one skips the OAuth step via foauth.org:

https://github.com/gulopine/foauth.org/issues/18#issuecomment-14015475

TODO:
====

* Restructure the proof of concept in proper entities/classes.
* See future thoughs in the code itself: https://github.com/brainstorm/kgantt/blob/master/kgantt.py#L42
