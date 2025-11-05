from PIL import Image
import sys
import os

def make_black_transparent(input_path, output_path=None, threshold=30):
    """
    使用PIL库将黑色背景透明化
    
    参数:
        input_path: 输入图片路径
        output_path: 输出图片路径（可选）
        threshold: 黑色阈值(0-255)，值越小越严格
    """
    try:
        # 打开图片并转换为RGBA模式
        img = Image.open(input_path).convert("RGBA")
        datas = img.getdata()
        
        new_data = []
        for item in datas:
            # 如果像素接近黑色(RGB值都很小)，则设为透明
            if item[0] <= threshold and item[1] <= threshold and item[2] <= threshold:
                new_data.append((255, 255, 255, 0))  # 完全透明
            else:
                new_data.append(item)  # 保持原样
        
        img.putdata(new_data)
        
        # 如果没有指定输出路径，在原文件名后添加_transparent
        if output_path is None:
            base_name = os.path.splitext(input_path)[0]
            output_path = f"{base_name}_transparent.png"
        
        img.save(output_path, "PNG")
        print(f"处理成功: {input_path} -> {output_path}")
        return True
        
    except Exception as e:
        print(f"处理失败: {e}")
        return False

def main():
    if len(sys.argv) < 2:
        print("用法: python black_transparent.py <图片路径> [输出路径] [阈值]")
        print("示例:")
        print("  python black_transparent.py input.jpg")
        print("  python black_transparent.py input.jpg output.png")
        print("  python black_transparent.py input.jpg output.png 50")
        return
    
    # 获取参数
    input_path = sys.argv[1]
    
    # 输出路径参数
    output_path = sys.argv[2] if len(sys.argv) > 2 else None
    
    # 阈值参数
    try:
        threshold = int(sys.argv[3]) if len(sys.argv) > 3 else 30
    except ValueError:
        print("错误: 阈值必须是数字")
        return
    
    # 检查输入文件是否存在
    if not os.path.exists(input_path):
        print(f"错误: 文件不存在 - {input_path}")
        return
    
    # 处理图片
    make_black_transparent(input_path, output_path, threshold)

if __name__ == "__main__":
    main()
