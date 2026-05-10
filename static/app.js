const fileInput = document.getElementById("image-input");
const dropzone = document.getElementById("dropzone");
const previewImage = document.getElementById("preview-image");
const clearButton = document.getElementById("clear-button");

function ensurePlaceholder() {
    let placeholder = document.getElementById("preview-placeholder");

    if (!placeholder) {
        placeholder = document.createElement("div");
        placeholder.id = "preview-placeholder";
        placeholder.className = "dropzone-placeholder";
        placeholder.innerHTML = `
            <div class="placeholder-icon"></div>
            <p class="placeholder-title">Drop casting image here</p>
            <p class="placeholder-subtitle">or click to browse files</p>
            <p class="placeholder-meta">PNG, JPG, JPEG, BMP</p>
        `;
    }

    return placeholder;
}

function showPreview(file) {
    if (!file) {
        return;
    }

    const previewShell = previewImage.parentElement;
    const placeholder = document.getElementById("preview-placeholder");
    const imageUrl = URL.createObjectURL(file);

    previewImage.src = imageUrl;
    previewImage.hidden = false;
    previewShell.classList.add("has-image");

    if (placeholder) {
        placeholder.remove();
    }
}

function clearPreview() {
    const previewShell = previewImage.parentElement;
    const placeholder = ensurePlaceholder();

    previewImage.hidden = true;
    previewImage.removeAttribute("src");
    previewShell.classList.remove("has-image");

    if (!document.getElementById("preview-placeholder")) {
        previewShell.appendChild(placeholder);
    }

    fileInput.value = "";
}

fileInput?.addEventListener("change", (event) => {
    const [file] = event.target.files;
    showPreview(file);
});

["dragenter", "dragover"].forEach((eventName) => {
    dropzone?.addEventListener(eventName, (event) => {
        event.preventDefault();
        dropzone.classList.add("dragover");
    });
});

["dragleave", "drop"].forEach((eventName) => {
    dropzone?.addEventListener(eventName, (event) => {
        event.preventDefault();
        dropzone.classList.remove("dragover");
    });
});

dropzone?.addEventListener("drop", (event) => {
    const [file] = event.dataTransfer.files;

    if (!file) {
        return;
    }

    const transfer = new DataTransfer();
    transfer.items.add(file);
    fileInput.files = transfer.files;
    showPreview(file);
});

clearButton?.addEventListener("click", () => {
    clearPreview();
});
