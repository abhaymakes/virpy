// const template = document.createElement("template");
// template.innerHTML = `
//     <aside class="w-64 bg-white shadow-md flex flex-col p-6">
//     <div class="flex items-center space-x-2 mb-8">
//         <h1 class="text-xl font-bold">Virpy</h1>
//     </div>
    
//     <!-- Navigation -->
//     <nav class="flex-1">
//         <h2 class="text-gray-400 text-sm uppercase mb-3">Scanning</h2>
//         <ul>
//             <li class="mb-2">
//                 <a href="#" class="flex items-center text-purple-600 font-semibold">
//                     <span>File Scanning</span>
//                 </a>
//             </li>
//             <li class="mb-2">
//                 <a href="#" class="flex items-center text-gray-500 hover:text-purple-600">
//                     <span>URL Scanning</span>
//                 </a>
//             </li>
//             <li class="mb-6">
//                 <a href="#" class="flex items-center text-gray-500 hover:text-purple-600">
//                     <span>IP Scanning</span> 
//                 </a>
//             </li>
//         </ul>
//         <h2 class="text-gray-400 text-sm uppercase mb-3">General</h2>
//         <ul>
//             <li class="mb-2">
//                 <a href="#" class="flex items-center text-gray-500 hover:text-purple-600">
//                     <span>Get Help</span>
//                 </a>
//             </li>
//             <li>
//                 <a href="#" class="flex items-center text-gray-500 hover:text-purple-600">
//                     <span>Settings</span> 
//                 </a>
//             </li>
//         </ul>
//     </nav>
    
//     <!-- Footer -->
//     <div class="text-center text-sm text-gray-500 mt-auto">
//         <p>Made by <span class="text-black font-medium">Abhay</span> <span class="text-red-500">❤</span></p>
//         <p>version 1.0</p>
//     </div>
// </aside>
// `;

// class SideBar extends HTMLElement {
//     constructor() {
//         super();
//         this.attachShadow({ mode: "open" }).appendChild(template.content.cloneNode(true));
//     }
// }

// customElements.define("sidebar-component", SideBar);






class SideBar extends HTMLElement {
    connectedCallback() {
        this.innerHTML = `
<aside class="w-56 bg-white shadow-md flex flex-col p-6 h-full">
    <div class="flex items-center space-x-2 mb-8">
        <h1 class="text-xl font-bold">Virpy</h1>
    </div>
    
    <!-- Navigation -->
    <nav class="flex-1">
        <h2 class="text-gray-400 text-sm uppercase mb-3">Scanning</h2>
        <ul>
            <li class="mb-2">
                <a href="/" class="flex items-center text-purple-600 font-semibold">
                   <i data-feather="file-text"></i>
                    <span>File Scanning</span>
                </a>
            </li>
            <li class="mb-2">
                <a href="/url" class="flex items-center text-gray-500 hover:text-purple-600">
                    <i data-feather="link-2"></i>

                    <span>URL Scanning</span>
                </a>
            </li>
            <li class="mb-6">
                <a href="/ip" class="flex items-center text-gray-500 hover:text-purple-600">
                    <i data-feather="globe"></i>

                    <span>IP Scanning</span> 
                </a>
            </li>
        </ul>
        <h2 class="text-gray-400 text-sm uppercase mb-3">General</h2>
        <ul>
            <li class="mb-2">
                <a href="/help" class="flex items-center text-gray-500 hover:text-purple-600">
                    <i data-feather="help-circle"></i>

                    <span>Get Help</span>
                </a>
            </li>
            <li>
                <a href="/settings" class="flex items-center text-gray-500 hover:text-purple-600">
                    <i data-feather="settings"></i>

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
`
    }

}


customElements.define("sidebar-component", SideBar);
