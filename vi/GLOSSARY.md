# Thuật ngữ khóa và ràng buộc bản dịch tiếng Việt

## Ràng buộc toàn cục

- Dịch sát nghĩa. Giữ số tiền, đơn vị `¥` / `元`, tên nền tảng Trung Quốc, luật và ví dụ thị trường Trung Quốc. Không đổi sang VND, Zalo, Shopee, Facebook Việt Nam.
- Không thêm bước thao tác, công cụ, hay cảnh báo mà bản gốc không có. Chương vùng xám (đại luyện game, cho vay, chứng khoán) chỉ dịch lại đúng những gì đã viết.
- Giữ nguyên tên riêng và mã kỹ thuật: MVP, CAC, LTV, ROI, SOP, PMF, ARR, MAU, OKR, KPI, SAFE, VIE, ESOP, GDPR, CCPA, ODI, PLG, SLG, Next.js, Whisper, FFmpeg, DeepSeek, GPT-4o, OpenClaw, Claude Code, Prisma, PostgreSQL, Flux, Midjourney, Stripe, PayPal.
- Lần đầu một từ viết tắt xuất hiện trong một chương, thêm nghĩa tiếng Việt trong ngoặc. Các lần sau trong cùng chương chỉ giữ từ viết tắt. Ví dụ: `PMF (khớp sản phẩm–thị trường)`.
- Giữ nguyên URL, kể cả URL Trung Quốc (`amazon.cn`, `juejin.cn`, `csdn.net`, `jobleap.cn`). Không dịch text trong URL.
- Giữ ký hiệu `¥` và mọi chuỗi số (số nguyên, thập phân, khoảng, phần trăm) đúng như bản gốc.
- Giữ cấp heading, số mục danh sách, bảng, in đậm theo cấu trúc bản gốc. Được phép câu tiếng Việt tự nhiên. Không được gộp hoặc bỏ mục.
- Tên file chương không đổi, gồm `ch0062-f.md` và `ch0140-f.md`. Không tạo chương còn thiếu: `ch0012`, `ch0013`, `ch0044`, `ch0135`.
- Không dịch: `LICENSE` (cả hai bản, Apache-2.0), `CLAUDE.md`, `README_en.md`, `README_jp.md`, `README_kr.md`, `DATA_UPDATE.md`, `.github/workflows/task.yml`, `.gitignore`, `程序员的副业赚钱宝典/mystyle.css`.
- Không sửa file tiếng Trung. Liên kết từ README gốc sang `vi/` là một bước riêng, chỉ làm khi anh yêu cầu thêm.
- Giọng: thẳng, có số, dạng SOP. Không thêm câu khích lệ, không thêm “nói ngắn gọn”, không viết lại cho hay hơn bản gốc.

## Bảng thuật ngữ khóa

Ghi đầy đủ vào `vi/GLOSSARY.md` ở Task 1. Các mục dưới đây là bắt buộc, không được mỗi lô một kiểu.

| Tiếng Trung | Tiếng Việt trong bài |
|---|---|
| 副业 | việc tay trái |
| 程序员 | lập trình viên |
| 生意思维 | tư duy kinh doanh |
| 技术思维 | tư duy kỹ thuật |
| 变现 | biến thành tiền |
| 冷启动 | khởi động lạnh |
| 获客 | tìm khách |
| 私域 | kênh riêng |
| 公域 | kênh công khai |
| 截流 | đón traffic |
| 投流 | chạy quảng cáo |
| 定价 | giá bán |
| 投入成本 / 启动成本 | chi phí ban đầu |
| 回本周期 | thời gian hòa vốn |
| 利润率 | tỷ suất lợi nhuận |
| 毛利率 | biên lợi nhuận gộp |
| 北极星指标 | chỉ số sao Bắc Đẩu |
| 避坑 | bẫy cần tránh |
| 账本 | sổ tài chính |
| 标题： | Tiêu đề: |
| 网友投稿： | Bạn đọc gửi: |
| 回复： | Trả lời: |
| 微信 / 微信群 | WeChat / nhóm WeChat |
| 企业微信 / 企微 | WeCom |
| 公众号 | tài khoản công khai WeChat |
| 视频号 | WeChat Channels |
| 小程序 | mini program |
| 抖音 | Douyin |
| 快手 | Kuaishou |
| 小红书 | Xiaohongshu |
| 闲鱼 | Xianyu |
| 淘宝 | Taobao |
| 1688 | 1688 |
| 京东 | JD.com |
| 拼多多 | Pinduoduo |
| 支付宝 | Alipay |
| 知乎 | Zhihu |
| 即刻 | Jike |
| B站 | Bilibili |
| 知识星球 | Knowledge Planet |
| 飞书 | Feishu |
| 小宇宙 | Xiaoyuzhou |

Không giữ chữ Hán trong bản Việt, trừ khi chữ đó nằm trong URL.

## Cách dịch và kiểm tra

- Ánh xạ cố định: `README.md` → `vi/README.md`; `程序员的副业赚钱宝典/<file>.md` → `vi/handbook/<file>.md`; `创业者早期的烦恼树洞/<file>.md` → `vi/founder/<file>.md`. Giữ nguyên tên file, kể cả `ch0062-f.md` và `ch0140-f.md`.
- Chương sổ tay dùng `--kind handbook`. Chương hỏi–đáp dùng `--kind founder-qa` và phải có đúng ba nhãn `Tiêu đề:`, `Bạn đọc gửi:`, `Trả lời:`. `创业者早期的烦恼树洞/ch0037.md`, `ch0038.md` và `README.md` dùng `--kind founder-free`. `README.md` gốc dùng `--kind readme`.
- Kiểm tra một cặp: `python3 scripts/qa_vi_translation.py <nguồn.md> <đích.md> --kind handbook|founder-qa|founder-free|readme`. PASS là thoát 0; FAIL kèm lý do là thoát 1.
- Kiểm tra cả cây: `python3 scripts/qa_vi_translation.py --tree`. Báo từng file đích còn thiếu và mọi `ch*.md` ở `vi/handbook/` hoặc `vi/founder/` mà nguồn không có. `vi/GLOSSARY.md` không phải bản dịch, không bắt buộc với `--tree`.
- Giữ mọi URL `http://` và `https://` của nguồn đúng ký tự và đúng số lần. Giữ đa tập chuỗi số (số nguyên, `1,500`, `9.9`) và số lần ký hiệu `¥`. Giữ số heading từng cấp `#` đến `######`, và số dòng bảng (dòng có `|` sau khoảng trắng đầu dòng).
- Không thêm `Zalo`, `Shopee`, `MoMo`, `VNĐ`, `VND` vào bản dịch (không phân biệt hoa thường). Nếu nguồn đã chứa một trong các từ này, giữ đúng số lần xuất hiện; không được thêm mới hay bỏ đi. Không đổi nền tảng hoặc đơn vị tiền sang thị trường Việt Nam.
- `万` = vạn. `亿` = trăm triệu, so `100亿` stays `100 trăm triệu` (10 tỷ) and `10亿` stays `10 trăm triệu` (1 tỷ). Do not translate `亿` as `ức`.
- `市场空间` = dư địa thị trường. Không dịch thành khoảng trống.
- `支撑` một ước lượng hoặc một quyết định = làm chỗ dựa cho quyết định đó. Không dịch thành chống.
- `自发推荐` = người dùng tự giới thiệu sản phẩm cho người khác. Không dịch thành tự giới thiệu bản thân.
- `对赌` / `业绩对赌` = đánh cược theo thành tích. Không dịch thành đối đầu.
- `风口` = ngành đang nóng / cơ hội đang lên. Không dịch thành làn gió.
- `亚逊小队` không phải tên tắt của Amazon. Giữ «tiểu đội Yaxun». Không thêm tên công ty.
