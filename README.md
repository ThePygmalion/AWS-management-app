# AWS Management Application

The AWS Management Application is a graphical user interface (GUI) tool built in Python using the `tkinter` library for managing various aspects of your Amazon Web Services (AWS) resources, specifically Amazon EC2 instances and Amazon RDS (Relational Database Service) resources.

## Features

### EC2 Management

1. **Create Snapshot**: Create snapshots for your Amazon EC2 instances with a custom description.
2. **Delete Snapshot**: Delete snapshots of Amazon EC2 instances.
3. **Delete Instances without Tag**: Terminate EC2 instances that do not have a specified tag.
4. **Stop Useless Instances**: Stop running EC2 instances that are considered "useless."

### RDS Management

1. **Delete RDS Instance**: Delete Amazon RDS instances.
2. **Delete RDS Cluster**: Delete Amazon RDS clusters.
3. **Stop Useless RDS**: Stop running Amazon RDS instances and clusters that are considered "useless."
4. **Delete Useless Snapshots**: Delete Amazon RDS snapshots that are no longer needed.
5. **Delete RDS without Tag**: Delete Amazon RDS instances and clusters that do not have a specified tag.
6. **Delete Old Snapshots**: Delete Amazon RDS snapshots that are older than a specified timeframe.

## Getting Started

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/aws-management-app.git
   ```

2. Install the required dependencies:

   ```bash
   pip install boto3
   ```

3. Configure your AWS credentials using the AWS CLI or by setting the necessary environment variables.

4. Run the application:

   ```bash
   python main.py
   ```

## Usage

1. Launch the application and use the GUI to select the desired AWS management action.
2. Follow the prompts and provide the necessary input, such as instance IDs, snapshot descriptions, etc.
3. The application will interact with your AWS account using the Boto3 library to perform the specified actions.

## Important Notes

- **Caution**: This application performs actions on your AWS resources. Always double-check your inputs and actions before confirming.
- **Security**: Ensure that your AWS credentials are properly secured and not exposed in your code or repository.
- **Customization**: You can customize and extend the application's functionality by modifying the `aws_script.py` file.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

This project was inspired by the need for an easy-to-use tool to manage AWS resources through a graphical interface.

---