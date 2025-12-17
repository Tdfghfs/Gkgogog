const out = document.getElementById("output");

function genEmail() {
    fetch("/gen")
        .then(r => r.json())
        .then(d => {
            if (d.status === "ok") {
                out.innerText = "📩 البريد:\n" + d.email;
            } else {
                out.innerText = "❌ خطأ";
            }
        });
}

function getMessages() {
    fetch("/get")
        .then(r => r.json())
        .then(d => {
            if (d.status === "ok") {
                if (d.messages.length === 0) {
                    out.innerText = "📭 لا توجد رسائل";
                } else {
                    let txt = "";
                    d.messages.forEach(m => {
                        txt += "📌 العنوان: " + m.subject + "\n";
                        txt += "📨 النص:\n" + m.body_text + "\n";
                        txt += "----------------------\n";
                    });
                    out.innerText = txt;
                }
            } else {
                out.innerText = d.msg;
            }
        });
}

function deleteAccount() {
    fetch("/delete")
        .then(r => r.json())
        .then(d => {
            out.innerText = "🗑️ تم حذف الحساب";
        });
}
