# ReverseIP Project

This project sets up an AWS EKS cluster named "revip-cluster" in the "ap-south-1" region using eksctl. It then deploys a Fargate profile named "revip-app" for the "revip" namespace to run the application. The application is deployed using Kubernetes manifests defined in the `deployment.yml` file located in the `k8s` directory of the project.

## Prerequisites

Before running the deployment commands, ensure you have the following prerequisites:

- AWS CLI configured with appropriate permissions.
- eksctl installed locally or available in your environment.
- kubectl installed locally or available in your environment.
- Helm installed locally or available in your environment.

## Deployment Steps

1. Update kubeconfig for the EKS cluster:
   ```bash
   aws eks update-kubeconfig --name revip-cluster --region ap-south-1


2. Create a Fargate profile for the application:
    ```bash
    eksctl create fargateprofile --cluster revip-cluster --region ap-south-1 --name revip-app --namespace revip

3. Deploy the application using Kubernetes manifests:
    ```bash
    kubectl apply -f https://raw.githubusercontent.com/prabhjot219/reverseip/main/k8s/deployment.yml


4. Configure IAM settings for the EKS cluster:
    ```bash
    cluster_name=my-cluster
    oidc_id=$(aws eks describe-cluster --name $cluster_name --query "cluster.identity.oidc.issuer" --output text | cut -d '/' -f 5)
    aws iam list-open-id-connect-providers | grep $oidc_id | cut -d "/" -f4
    eksctl utils associate-iam-oidc-provider --cluster $cluster_name --approve

5. Create IAM policies and roles for the AWS Load Balancer Controller:
    ```bash
    curl -O https://raw.githubusercontent.com/kubernetes-sigs/aws-load-balancer-controller/v2.5.4/docs/install/iam_policy.json
    aws iam create-policy --policy-name AWSLoadBalancerControllerIAMPolicy --policy-document file://iam_policy.json
    eksctl create iamserviceaccount --cluster=revip-cluster --namespace=kube-system --name=aws-load-balancer-controller --role-name AmazonEKSLoadBalancerControllerRole --attach-policy-arn=arn:aws:iam::<aws account id>:policy/AWSLoadBalancerControllerIAMPolicy --approve --override-existing-serviceaccounts

6. Install the AWS Load Balancer Controller using Helm:
    ```bash
    helm repo add eks https://aws.github.io/eks-charts
    helm repo update eks
    helm install aws-load-balancer-controller eks/aws-load-balancer-controller -n kube-system --set clusterName=reverseip-cluster --set serviceAccount.create=false --set serviceAccount.name=aws-load-balancer-controller --set region=ap-south-1 --set vpcId=<vpc id>

7. Continuous Integration and Continuous Delivery (CI/CD)

This project utilizes GitHub Actions for Continuous Integration (CI) and Continuous Delivery (CD) pipelines. The CI/CD pipelines are automatically triggered on every push to the main branch, ensuring automated deployment of changes.