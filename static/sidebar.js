class SideBar extends HTMLElement {
    connectedCallback() {
        this.innerHTML = `
// <aside class="w-56 bg-white shadow-md flex flex-col p-6 h-full sticky top-0">
<aside class="w-56 fixed top-0 left-0 h-screen bg-white shadow-md flex flex-col p-6 z-20">
    <div class="flex items-center space-x-2 mb-8">
        <h1 class="text-xl font-bold">Virpy</h1>
    </div>
    
    <!-- Navigation -->
    <nav class="flex-1">
        <h2 class="text-gray-400 text-sm uppercase mb-3">Scanning</h2>
        <ul>
            <li class="mb-2">
                <a href="/" class="nav-link flex items-center gap-2 px-3 py-2 rounded-md hover:bg-purple-50 hover:text-purple-600 text-gray-500">
                    <i data-feather="file-text" class="w-4 h-4"></i>
                    <span>Scanning</span>
                </a>
            </li>
        </ul>
        <h2 class="text-gray-400 text-sm uppercase mb-3">General</h2>
        <ul>
            <li class="mb-2">
                <a href="/help" class="nav-link flex items-center gap-2 px-3 py-2 rounded-md hover:bg-purple-50 hover:text-purple-600 text-gray-500">
                    <i data-feather="help-circle" class="w-4 h-4"></i>
                    <span>Get Help</span>
                </a>
            </li>
            <li>
                <a href="/settings" class="nav-link flex items-center gap-2 px-3 py-2 rounded-md hover:bg-purple-50 hover:text-purple-600 text-gray-500">
                    <i data-feather="settings" class="w-4 h-4"></i>
                    <span>Settings</span>
                </a>
            </li>
        </ul>
    </nav>
    
    <!-- Footer -->
    <div class="text-center text-sm text-gray-500 mt-auto">
        <p>Made by <span class="text-black font-medium">Abhay</span> <span class="text-red-500">❤</span></p>
        <p>version 1.0</p>
    </div>
</aside>
        `;

        feather.replace();

        // Highlight active link
        const currentPath = window.location.pathname;
        const links = this.querySelectorAll('.nav-link');
        links.forEach(link => {
            if (link.getAttribute('href') === currentPath) {
                link.classList.add('bg-purple-50', 'text-purple-600', 'font-semibold', 'shadow-sm');
            } else {
                link.classList.remove('bg-purple-50', 'text-purple-600', 'font-semibold', 'shadow-sm');
            }
        });
    }
}

customElements.define("sidebar-component", SideBar);
