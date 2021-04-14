#! /usr/bin/env bash
rsync -arvzh --delete --exclude "notebooks/*" --exclude "data/*" . desktop:/root/personal_projects/trading
