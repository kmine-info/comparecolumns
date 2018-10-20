#!/bin/bash
export PROJECT_FOLDER=/kmine/Vlookup
export LOG_FOLDER=$PROJECT_FOLDER/logs
export ERROR_LOG=$LOG_FOLDER/gunicorn.log
export ACCESS_LOG=$LOG_FOLDER/access.log
#export SOCKET_FILE=$





# Prepare log files
touch $ERROR_LOG
touch $ERROR_LOG

#start outputting logs to stdout but this process runs in background

tail -n 0 -f $LOG_FOLDER/*.log &


echo Starting nginx 


# Start Gunicorn processes
echo Starting Gunicorn.


cd $PROJECT_FOLDER/src

/venv/bin/python manage.py migrate        # Apply database migrations
#/venv/bin/python manage.py collectstatic --clear --noinput # clearstatic files
#/venv/bin/python manage.py collectstatic --noinput  # collect static files



exec /venv/bin/gunicorn VLookUp.wsgi:application \
    --log-file=$ERROR_LOG \
    --access-logfile=$ACCESS_LOG  \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --log-level=info \
    #--daemon 

        #--name VLookUp \   # Name of this Gunicorn Application
    #--bind unix:vlookup_app.sock \ # Binding to a local Unix Socket File
#- \

#exec service nginx start
