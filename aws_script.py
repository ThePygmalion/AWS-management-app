import boto3
import datetime

# Initialize AWS clients
ec2_client = boto3.client('ec2')
rds_client = boto3.client('rds')

# EC2 Management

# 1. Create your own Key based SnapShots
def create_snapshot(instance_id, snapshot_description):
    response = ec2_client.create_snapshot(
        Description=snapshot_description,
        VolumeId=instance_id
    )
    return response['SnapshotId']

# 2. Delete SnapShots
def delete_snapshot(snapshot_id):
    ec2_client.delete_snapshot(SnapshotId=snapshot_id)

# 3. Delete/Terminate EC2 instances without a specific tag
def delete_instances_without_tag(tag_key):
    instances = ec2_client.describe_instances(
        Filters=[{'Name': 'tag-key', 'Values': [tag_key]}]
    )
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            ec2_client.terminate_instances(InstanceIds=[instance_id])

# 4. Stop useless running EC2 instances
def stop_useless_instances():
    instances = ec2_client.describe_instances(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
    )
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            ec2_client.stop_instances(InstanceIds=[instance_id])

# RDS Management

# 1. Delete RDS Instance
def delete_rds_instance(instance_id):
    rds_client.delete_db_instance(DBInstanceIdentifier=instance_id, SkipFinalSnapshot=True)

# 2. Delete RDS Cluster
def delete_rds_cluster(cluster_id):
    rds_client.delete_db_cluster(DBClusterIdentifier=cluster_id, SkipFinalSnapshot=True)

# 3. Stop useless running RDS instances/clusters
def stop_useless_rds():
    instances = rds_client.describe_db_instances()
    clusters = rds_client.describe_db_clusters()
    
    for instance in instances['DBInstances']:
        instance_id = instance['DBInstanceIdentifier']
        if instance['DBInstanceStatus'] == 'available':
            rds_client.stop_db_instance(DBInstanceIdentifier=instance_id)
    
    for cluster in clusters['DBClusters']:
        cluster_id = cluster['DBClusterIdentifier']
        if cluster['Status'] == 'available':
            rds_client.stop_db_cluster(DBClusterIdentifier=cluster_id)

# 4. Delete useless snapshots
def delete_useless_snapshots():
    snapshots = rds_client.describe_db_snapshots()
    for snapshot in snapshots['DBSnapshots']:
        snapshot_id = snapshot['DBSnapshotIdentifier']
        rds_client.delete_db_snapshot(DBSnapshotIdentifier=snapshot_id)

# 5. Delete RDS instances/clusters without a specific tag
def delete_rds_without_tag(tag_key):
    instances = rds_client.describe_db_instances()
    clusters = rds_client.describe_db_clusters()
    
    for instance in instances['DBInstances']:
        instance_id = instance['DBInstanceIdentifier']
        tags = rds_client.list_tags_for_resource(ResourceName=instance['DBInstanceArn'])['TagList']
        if not any(tag['Key'] == tag_key for tag in tags):
            delete_rds_instance(instance_id)
    
    for cluster in clusters['DBClusters']:
        cluster_id = cluster['DBClusterIdentifier']
        tags = rds_client.list_tags_for_resource(ResourceName=cluster['DBClusterArn'])['TagList']
        if not any(tag['Key'] == tag_key for tag in tags):
            delete_rds_cluster(cluster_id)

# 6. Delete RDS snapshots older than 2 days
def delete_old_snapshots():
    snapshots = rds_client.describe_db_snapshots()
    cutoff_date = datetime.datetime.now() - datetime.timedelta(days=2)
    
    for snapshot in snapshots['DBSnapshots']:
        snapshot_id = snapshot['DBSnapshotIdentifier']
        snapshot_create_time = snapshot['SnapshotCreateTime']
        
        if snapshot_create_time < cutoff_date:
            rds_client.delete_db_snapshot(DBSnapshotIdentifier=snapshot_id)

# Example usage
if __name__ == '__main__':
    # EC2
    create_snapshot('your-instance-id', 'My Snapshot Description')
    delete_snapshot('your-snapshot-id')
    delete_instances_without_tag('my-tag-key')
    stop_useless_instances()
    
    # RDS
    delete_rds_instance('your-instance-id')
    delete_rds_cluster('your-cluster-id')
    stop_useless_rds()
    delete_useless_snapshots()
    delete_rds_without_tag('my-tag-key')
    delete_old_snapshots()
