#!/bin/bash

# get the running script file full path
get_script_dir() {
    oldwd=`pwd`
    rw=`dirname $0`
    cd $rw
    sw=`pwd`
    cd $oldwd
    echo $sw
}

RUN_PATH=`get_script_dir`
APP_PATH=`dirname $RUN_PATH`
MAIN_APP=$APP_PATH/wx_pay/restapi/wx_pay_agent.py

app_pid=0
check_pid() {
    UNIX_PS=`ps -ef | grep $MAIN_APP | grep -v 'grep'`
    if [ -n "$UNIX_PS" ]; then
        app_pid=`echo $UNIX_PS | awk '{print $2}'`
    else
        app_pid=0
    fi
}

check_pid

if [ $app_pid -ne 0 ]; then
    echo "================================"
    echo "$MAIN_APP is running"
    echo "================================"
else
    echo "================================"
    echo "$MAIN_APP is stopped"
    echo "================================"
fi

exit 0
