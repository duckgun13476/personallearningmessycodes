from minio import Minio
from minio.error import S3Error


#  用于获取minio存储桶的体积
def get_bucket_size(client, bucket_name_2):
    try:
        objects = client.list_objects(bucket_name_2)
        total_size = sum(obj.size for obj in objects if obj.size is not None)
        return total_size
    except S3Error as e:
        print("S3 error: ", e)

def format_size(size_bytes):
    if size_bytes < 1024:
        return f"{size_bytes} bytes"
    elif size_bytes < 1024 ** 2:
        return f"{size_bytes / 1024:.3f} KB"
    elif size_bytes < 1024 ** 3:
        return f"{size_bytes / 1024 ** 2:.3f} MB"
    else:
        return f"{size_bytes / 1024 ** 3:.3f} GB"

def read_bucket_size():
    # 创建 MinIO 客户端实例
    client = Minio(
        "192.168.147.107:9500",  # 替换为您的 MinIO 服务器地址
        access_key="uL0hh3dlU2hq5i6ZKXFj",  # 替换为您的 access key
        secret_key="mkWiZt5niwgqZkBRz4I8HZGB8p1gI6fMHrcb39OJ",  # 替换为您的 secret key
        secure=False  # 设置为 True 如果是 HTTPS，否则设置为 False
    )

    # 获取 bucket 的容量
    bucket_name_1 = "usedfor-s-three-test"  # 替换为您要查询的 bucket 名称
    bucket_size_1 = get_bucket_size(client, bucket_name_1)
    bucket_size_1=format_size(bucket_size_1)
    return bucket_size_1, bucket_name_1


if __name__ == '__main__':
    bucket_size, bucket_name = read_bucket_size()
    if bucket_size is not None:
        print(f"存储桶 '{bucket_name}' 已使用: {bucket_size} ")
