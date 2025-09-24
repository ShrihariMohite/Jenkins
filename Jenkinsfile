stage('Build') {
    steps {
        echo 'Building Docker image...'
        sh 'sudo docker build -t myapp:latest .'
    }
}
stage('Deploy') {
    steps {
        echo 'Deploying container...'
        sh '''
        sudo docker rm -f myapp-container || true
        sudo docker run -d -p 8081:8080 --name myapp-container myapp:latest
        '''
    }
}
