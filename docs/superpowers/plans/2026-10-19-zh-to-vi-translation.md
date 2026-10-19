# Kế hoạch dịch repo từ tiếng Trung sang tiếng Việt

> **Dành cho agent thực thi:** Chưa dịch khi kế hoạch này chưa được duyệt. Khi được duyệt, dùng `superpowers:executing-plans` (một phiên, lần lượt) hoặc `superpowers:subagent-driven-development` (mỗi lô một agent, có reviewer). Các bước dùng `- [ ]`.

**Mục tiêu:** Có một bản tiếng Việt đọc được, bám sát nghĩa, của toàn bộ nội dung tiếng Trung trong repo, đặt cạnh bản gốc, không sửa bản gốc.

**Kiến trúc:** Bản Trung vẫn là nguồn. Bản Việt nằm dưới `vi/`, giữ nguyên mã chương `ch####.md`. Một bảng thuật ngữ khóa và một script kiểm tra (số, URL, cấu trúc Markdown, chữ Hán sót) chạy sau mỗi lô. Dịch sát, không viết lại cho thị trường Việt Nam.

**Tech stack:** Markdown, Python 3 (script QA), Git. Không thêm framework, không dịch bằng cách sửa file nguồn.

**Spec:** Kế hoạch này đồng thời là spec. Các quyết định đã chốt nằm ở mục Ràng buộc. Nếu anh đổi một quyết định, sửa mục đó trước khi dịch.

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

## Phạm vi đã đo (2026-10-19)

| Nhóm | File `.md` | Chữ Hán | Ghi chú |
|---|---:|---:|---|
| `程序员的副业赚钱宝典/` | 444 chương | ~567.000 | ch0001–ch0448, thiếu 12, 13, 44, 135; thêm `ch0062-f.md`, `ch0140-f.md` |
| `创业者早期的烦恼树洞/` | 70 chương + `README.md` | ~33.500 | 68 chương dạng hỏi–đáp; `ch0037.md` và `ch0038.md` lệch khuôn |
| `README.md` | 1 | ~1.900 | Mục lục một phần, không liệt kê hết 444 chương |
| Còn lại | 6 | ít | EN/JP/KR README, `CLAUDE.md`, `DATA_UPDATE.md` — ngoài phạm vi dịch |

Tổng nội dung cần dịch: **516 file**, khoảng **604.000 chữ Hán**, khoảng **1,06 triệu ký tự** nguồn. Không có code fence, không có ảnh. 21 file có bảng. 82 liên kết Markdown, khoảng 16 liên kết trỏ tới file chương. 362 file có `¥` hoặc `元`.

Hai khuôn bài:

- **SOP (415 chương sổ tay):** thường có nhu cầu, MVP, traffic Trung Quốc, bảng tài chính, chỉ số, rủi ro, case. Mẫu rõ ở `ch0374.md`, `ch0443.md`.
- **Lệch SOP (29 chương sổ tay):** `ch0047.md`, `ch0081.md`–`ch0100.md`, `ch0232.md`, `ch0233.md`, `ch0235.md`, `ch0236.md`, `ch0239.md`, `ch0241.md`, `ch0245.md`, `ch0254.md`. Dịch theo cấu trúc riêng của từng file, không ép vào khung SOP.
- **Hỏi–đáp (68 chương cây lỗ):** mở đầu bằng `标题：`, rồi `网友投稿：`, rồi `回复：`. Giữ ba nhãn tiếng Việt cố định (xem bảng thuật ngữ).
- **Lệch khuôn cây lỗ:** `ch0037.md` (không có nhãn `标题：`), `ch0038.md` (bắt đầu bằng `## 内容`), `README.md` (danh sách sách, video, công cụ).

## Bố cục file

```
vi/
  README.md                 # bản của README.md gốc, link trỏ vào vi/
  GLOSSARY.md               # thuật ngữ khóa, không phải bản dịch
  handbook/                 # 程序员的副业赚钱宝典
    ch0001.md …             # cùng tên file nguồn
  founder/                  # 创业者早期的烦恼树洞
    README.md
    ch0001.md … ch0070.md
scripts/
  qa_vi_translation.py      # kiểm tra một file hoặc cả cây
```

Ánh xạ đường dẫn cố định:

| Nguồn | Đích |
|---|---|
| `README.md` | `vi/README.md` |
| `程序员的副业赚钱宝典/<file>.md` | `vi/handbook/<file>.md` |
| `创业者早期的烦恼树洞/<file>.md` | `vi/founder/<file>.md` |

Liên kết tương đối trong bản Việt viết lại theo ánh xạ này. Liên kết tuyệt đối (http/https) giữ nguyên.

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

## Review Focus

Năm lỗi dễ lọt mà đếm heading không bắt được. Mỗi lỗi có kiểm tra ở task sở hữu nó.

1. Số tiền bị đổi đơn vị hoặc làm tròn (`¥199` thành `199.000 đồng`). Script so đa tập chuỗi số và ký hiệu `¥`.
2. Nền tảng Trung Quốc bị thay bằng nền tảng Việt (WeChat thành Zalo). Script cấm một danh sách từ thay thế; người duyệt pilot đọc 6 file mẫu.
3. Chương hỏi–đáp mất một trong ba nhãn `Tiêu đề:` / `Bạn đọc gửi:` / `Trả lời:`. Script kiểm tra 68 file khuôn này.
4. URL hoặc tên repo GitHub bị “dịch” (`XiaomingX` thành tên khác, `amazon.cn` thành `amazon.com`). Script so danh sách URL.
5. Chương vùng xám bị viết thêm bước thực hiện. Pilot và mỗi lô có một file vùng xám được đối chiếu câu-đối-câu với nguồn; script không đủ cho lỗi này.

## Thứ tự làm

Làm đúng thứ tự. Không mở lô sổ tay trước khi anh duyệt giọng của 6 file pilot.

### Task 1: Hợp đồng dịch và script kiểm tra

**Files:**

- Create: `vi/GLOSSARY.md`
- Create: `scripts/qa_vi_translation.py`

**Interfaces:**

- Consumes: không có
- Produces: `qa_vi_translation.py <source.md> <vi.md> --kind handbook|founder-qa|founder-free|readme` in `PASS` hoặc `FAIL` kèm lý do. Exit 0 khi pass, exit 1 khi fail. Cờ `--tree` so toàn bộ ánh xạ và báo file thiếu hoặc file thừa.

- [ ] **Step 1: Viết `vi/GLOSSARY.md`**

Chép nguyên bảng thuật ngữ khóa ở trên. Thêm quy tắc ràng buộc toàn cục, rút thành các gạch đầu dòng người dịch có thể làm theo mà không cần đọc cả kế hoạch này.

- [ ] **Step 2: Viết `scripts/qa_vi_translation.py`**

Một file Python, chỉ thư viện chuẩn. Với một cặp file:

- Đích tồn tại và không rỗng.
- Đếm chữ Hán ở đích bằng 0 (dải U+4E00–U+9FFF).
- Mọi URL `http://` và `https://` ở nguồn xuất hiện ở đích, cùng số lần.
- Đa tập các chuỗi số (regex `\d+(?:[.,]\d+)*`) của nguồn và đích trùng nhau. Ký hiệu `¥` có cùng số lần.
- Số heading theo từng cấp `#` đến `######` trùng nhau.
- Số dòng bảng (dòng bắt đầu bằng `|`) trùng nhau.
- `--kind founder-qa`: đích chứa đúng các nhãn `Tiêu đề:`, `Bạn đọc gửi:`, `Trả lời:`.
- Cấm các chuỗi: `Zalo`, `Shopee`, `MoMo`, `VNĐ`, `VND`, `đồng` khi đi kèm số tiền đổi đơn vị. Cho phép chữ `đồng` chỉ khi nguồn đã nói về đồng tiền Việt. Cách làm chắc: cấm `Zalo`, `Shopee`, `MoMo`, `VNĐ`, `VND`.
- `--tree`: với mỗi `.md` nguồn trong ánh xạ, đích tồn tại; không có `ch*.md` ở đích mà nguồn không có.

- [ ] **Step 3: Chạy script khi chưa có bản dịch**

Run: `python3 scripts/qa_vi_translation.py --tree`

Expected: FAIL, liệt kê file đích còn thiếu. Không được báo PASS.

- [ ] **Step 4: Commit**

```bash
git add vi/GLOSSARY.md scripts/qa_vi_translation.py
git commit -m "Add Vietnamese translation glossary and QA script"
```

Chỉ commit khi anh đã bảo commit.

### Task 2: Sáu file pilot để khóa giọng

**Files:**

- Create: `vi/handbook/ch0001.md` từ `程序员的副业赚钱宝典/ch0001.md`
- Create: `vi/handbook/ch0374.md` từ `程序员的副业赚钱宝典/ch0374.md`
- Create: `vi/handbook/ch0081.md` từ `程序员的副业赚钱宝典/ch0081.md`
- Create: `vi/handbook/ch0099.md` từ `程序员的副业赚钱宝典/ch0099.md`
- Create: `vi/founder/ch0001.md` từ `创业者早期的烦恼树洞/ch0001.md`
- Create: `vi/founder/README.md` từ `创业者早期的烦恼树洞/README.md`

**Interfaces:**

- Consumes: `vi/GLOSSARY.md`, `qa_vi_translation.py`
- Produces: giọng mẫu. Các lô sau phải theo các file này.

`ch0099.md` là chương vùng xám (đại luyện game). Dịch đúng nội dung đang có. Không thêm bước, giá, hay mẹo mới.

- [ ] **Step 1: Dịch sáu file**

Dịch từng file một. Đọc nguồn hết rồi mới viết đích. Áp bảng thuật ngữ.

- [ ] **Step 2: Chạy QA từng cặp**

Run:

```bash
python3 scripts/qa_vi_translation.py "程序员的副业赚钱宝典/ch0001.md" vi/handbook/ch0001.md --kind handbook
python3 scripts/qa_vi_translation.py "程序员的副业赚钱宝典/ch0374.md" vi/handbook/ch0374.md --kind handbook
python3 scripts/qa_vi_translation.py "程序员的副业赚钱宝典/ch0081.md" vi/handbook/ch0081.md --kind handbook
python3 scripts/qa_vi_translation.py "程序员的副业赚钱宝典/ch0099.md" vi/handbook/ch0099.md --kind handbook
python3 scripts/qa_vi_translation.py "创业者早期的烦恼树洞/ch0001.md" vi/founder/ch0001.md --kind founder-qa
python3 scripts/qa_vi_translation.py "创业者早期的烦恼树洞/README.md" vi/founder/README.md --kind founder-free
```

Expected: mỗi lệnh in `PASS`.

- [ ] **Step 3: Dừng để anh đọc giọng**

Không dịch tiếp cho đến khi anh xác nhận sáu file này. Nếu anh sửa thuật ngữ, cập nhật `vi/GLOSSARY.md` trước khi sang Task 3.

### Task 3: Hết sách hỏi–đáp nhà sáng lập

**Files:**

- Create: `vi/founder/ch0002.md` … `vi/founder/ch0070.md`, trừ `ch0001.md` đã có ở Task 2
- `ch0037.md` dùng `--kind founder-free`
- `ch0038.md` dùng `--kind founder-free`
- 66 file còn lại dùng `--kind founder-qa`

**Interfaces:**

- Consumes: giọng `vi/founder/ch0001.md`, glossary, script QA
- Produces: đủ 70 chương + README dưới `vi/founder/`

- [ ] **Step 1: Dịch theo lô 10 chương**

Bảy lô: 0002–0011, 0012–0021, 0022–0031, 0032–0036 cộng 0037–0041, 0042–0051, 0052–0061, 0062–0070. Mỗi lô xong thì chạy QA cả lô trước khi sang lô sau.

- [ ] **Step 2: Đối chiếu tay hai chương lệch khuôn và một chương có lời quảng bá**

Đọc nguồn và đích của `ch0037.md`, `ch0038.md`, và một chương có chữ `jobleap.cn` (ví dụ `ch0030.md`). URL còn nguyên. Không thêm câu kết mới.

- [ ] **Step 3: Chạy `--tree` và xác nhận nhánh founder đủ file**

Expected: mọi file `创业者早期的烦恼树洞/*.md` có cặp ở `vi/founder/`. Nhánh handbook vẫn thiếu là đúng ở bước này.

### Task 4: Sổ tay lập trình viên, theo dải số

**Files:**

- Create: các `vi/handbook/ch*.md` còn lại, gồm `ch0062-f.md` và `ch0140-f.md`
- Không tạo file cho chương 12, 13, 44, 135

**Interfaces:**

- Consumes: giọng `vi/handbook/ch0001.md`, `ch0374.md`, `ch0081.md`, glossary, script
- Produces: 444 file chương dưới `vi/handbook/`

Mỗi lô là một đơn vị duyệt. Dải dưới đây đã trừ file pilot và chương không tồn tại.

- [ ] **Step 1: Lô A — ch0002–ch0046** (không có ch0012, ch0013; ch0001 đã xong)
- [ ] **Step 2: Lô B — ch0048–ch0080** (không có ch0044; ch0047 thuộc nhóm lệch SOP)
- [ ] **Step 3: Lô C — ch0082–ch0120** (ch0081 đã xong; cả cụm lệch SOP đến ch0100; không có ch0135 ở lô sau)
- [ ] **Step 4: Lô D — ch0121–ch0160** (không có ch0135; gồm `ch0140-f.md`)
- [ ] **Step 5: Lô E — ch0161–ch0200**
- [ ] **Step 6: Lô F — ch0201–ch0240** (gồm các chương lệch SOP 0232, 0233, 0235, 0236, 0239)
- [ ] **Step 7: Lô G — ch0241–ch0280** (gồm 0241, 0245, 0254)
- [ ] **Step 8: Lô H — ch0281–ch0320**
- [ ] **Step 9: Lô I — ch0321–ch0373** (ch0374 đã xong)
- [ ] **Step 10: Lô J — ch0375–ch0420**
- [ ] **Step 11: Lô K — ch0421–ch0448** (trừ ch0443 nếu đã dịch ở pilot; ch0443 thuộc pilot thì bỏ qua)

Sau mỗi lô:

```bash
python3 scripts/qa_vi_translation.py --tree
```

Expected của cả task khi xong: 444 cặp handbook PASS, không có file thừa.

Trong mỗi lô, chọn 1 chương có `¥` và đọc đối chiếu số tiền. Ở lô B hoặc lô nào chứa chương chứng khoán / cho vay (`ch0047.md`, `ch0092.md`), đối chiếu thêm để chắc không có câu hướng dẫn mới.

### Task 5: README gốc và liên kết

**Files:**

- Create: `vi/README.md` từ `README.md`

**Interfaces:**

- Consumes: ánh xạ đường dẫn, các chương đã dịch (tiêu đề chương trong README phải khớp tiêu đề đã dịch, không dịch lại một kiểu khác)
- Produces: README tiếng Việt với link nội bộ trỏ tới `vi/handbook/` và `vi/founder/`

- [ ] **Step 1: Dịch `README.md`**

Bốn link chương trong mục “程序员的副业赚钱宝典” đổi thành `handbook/ch0443.md` … `handbook/ch0446.md`. Anchor text dùng đúng H1 của file Việt đã có. Mọi URL `https://` giữ nguyên.

- [ ] **Step 2: QA**

Run: `python3 scripts/qa_vi_translation.py README.md vi/README.md --kind readme`

Expected: `PASS`.

- [ ] **Step 3: QA cả cây**

Run: `python3 scripts/qa_vi_translation.py --tree`

Expected: `PASS`, 516 cặp (444 handbook + 71 founder + 1 README gốc).

### Task 6: Đối chiếu người đọc

- [ ] **Step 1: Lấy mẫu 10 chương ngẫu nhiên ngoài pilot**

Đọc nguồn và đích cạnh nhau. Kiểm tra: nghĩa đoạn đầu và đoạn cuối còn đủ, số tiền không đổi, không có chữ Hán, giọng không bị thêm lời cổ vũ.

- [ ] **Step 2: Sửa các file fail**

Chỉ sửa đích. Chạy lại QA file đó đến khi `PASS`.

- [ ] **Step 3: Dừng**

Không sửa README tiếng Trung, không dịch LICENSE, không thêm chỉ mục 444 chương nếu nguồn không có.

## Việc cố ý không làm

- Không bản địa hóa sang thị trường Việt Nam.
- Không song ngữ trong cùng một file.
- Không thay bản Trung bằng bản Việt.
- Không dịch README tiếng Anh, Nhật, Hàn.
- Không viết chỉ mục mới cho 444 chương.
- Không đụng workflow cập nhật `DATA_UPDATE.md`.

## Ước lượng

- Task 1: một phiên ngắn.
- Task 2: một phiên, rồi chờ anh đọc.
- Task 3: một đến hai phiên.
- Task 4: phần lớn khối lượng. Khoảng 40 chương mỗi phiên nếu làm trong một phiên; hoặc 4 agent song song trên 4 lô khác nhau sau khi pilot đã được duyệt. Không cho hai agent sửa cùng một file.
- Task 5 và 6: một phiên.

Tổng thực tế phụ thuộc vào số vòng sửa giọng sau pilot. Nếu pilot phải sửa thuật ngữ, các lô đã dịch theo thuật ngữ cũ phải làm lại. Vì vậy không dịch trước Task 4 khi Task 2 chưa được gật đầu.
