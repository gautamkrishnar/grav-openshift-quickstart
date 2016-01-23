#!/bin/bash
#
# This is just a friendly notice page.
# Feel free to delete this file.
#

if [[ -x ${OPENSHIFT_HOMEDIR}/app-root/runtime/bin/php-cgi ]] ; then
    echo "Status: 302 Found"
    echo "Content-Type: text/html"
    echo ""
    echo '<meta http-equiv="refresh" content="0; url=index.php">'
    echo 'Please Refresh.'
    rm -f ${OPENSHIFT_REPO_DIR}/www/index.cgi
    exit 0
fi

echo "Content-Type: text/plain"
echo ""
echo "Your PHP environment is not ready yet, please wait..."
echo "It will finish in half an hour."
echo "Do NOT update / restart / stop your OpenShift App before it finishes."
echo ""
echo "-----------------------------------------------------"
echo ""
cat  /tmp/build_log

exit 0

