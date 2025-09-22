# cdk-s3-project

This project uses the AWS Cloud Development Kit (CDK) to set up an S3 bucket.

## Prerequisites

- Node.js (version 14.x or later)
- AWS CLI configured with appropriate permissions

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd cdk-s3-project
   ```

2. Install the dependencies:
   ```bash
   npm install
   ```

## Deploying the Stack

To deploy the stack, run the following command:

```bash
cdk deploy
```

This command will create the S3 bucket defined in the `CdkS3Stack` class.

## Running Tests

To run the unit tests for the stack, use the following command:

```bash
npm test
```

## Cleanup

To remove the stack and all associated resources, run:

```bash
cdk destroy
```

## License

This project is licensed under the MIT License.