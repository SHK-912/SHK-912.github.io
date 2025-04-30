import boto3
import csv
import io

def lambda_handler(event, context):
    # S3 정보
    bucket_name = 'your-bucket-name'
    key = 'path/to/your-file.csv'  # 예: 'data/sample.csv'

    # S3에서 객체 가져오기
    s3 = boto3.client('s3')
    response = s3.get_object(Bucket=bucket_name, Key=key)

    # 파일 내용 읽기 (UTF-8 assumed)
    file_content = response['Body'].read().decode('utf-8')
    
    # CSV 파싱
    reader = csv.DictReader(io.StringIO(file_content))
    rows = [row for row in reader]

    # 예시 출력 (CloudWatch Logs에서 확인 가능)
    for row in rows:
        print(row)

    return {
        'statusCode': 200,
        'body': f'Read {len(rows)} rows from CSV.'
    }
