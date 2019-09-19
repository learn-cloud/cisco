def result
pipeline {
agent any
stages {
    stage('Git-Checkout') {
        steps {
            script{
                 checkout scm
                 sh 'sudo sh /root/test-j.sh '
                 result = readFile('folder-list.txt').trim()
                 echo result
                }
            }
        }
    
    stage('Deploy CC') {
        steps {
            script { 
                if (result == 'CC') {
                    echo 'Changes Done in CC Folder'
                } else {
                    echo 'Changes not done in CC folder'
                    }
                }
            }
        }

    stage('Deploy DD') {
        steps {
            script { 
                if (result == 'DD') {
                    echo 'Changes Done in DD Folder'
                } else {
                    echo 'Changes not done in DD folder'
                    }
                }
            }
        }
    
    stage('Deploy EE') {
        steps {
            script { 
                if (result == 'EE') {
                    echo 'Changes Done in EE Folder'
                    sh 'pwd'
                    sh 'ls -ltr'
                    sh 'cd EE'
                    // sh 'export FLASK_APP=api.py'
                    // sh 'flask run --host 0.0.0.0 --port 5000'
                    sh 'python /var/lib/jenkins/workspace/cisco-test/EE/api.py '
                } else {
                    echo 'Changes not done in EE folder'
                    }
                }
            }
        }
    }
}
