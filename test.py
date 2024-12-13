from bs4 import BeautifulSoup

f = """
<div class="card w-100">
   <div class="card-header hstack flex-wrap justify-content-between gap-2">
      \x3C!--?lit$192891070$--> 
      <div class="hstack gap-2 fw-bold text-danger">
         <i class="fs-4 hstack">
            \x3C!--?lit$192891070$-->\x3C!--?lit$192891070$-->
            <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24" fill="currentColor">
               \n  
               <path d="M11.997 16.63c.22 0 .404-.073.55-.217a.738.738 0 0 0 .22-.548.751.751 0 0 0-.217-.55.738.738 0 0 0-.547-.22.751.751 0 0 0-.55.217.737.737 0 0 0-.22.548.75.75 0 0 0 .764.77Zm-.686-3.553h1.399v-5.92h-1.4v5.92Zm.691 8.221a9.05 9.05 0 0 1-3.626-.733 9.395 9.395 0 0 1-2.954-1.99 9.407 9.407 0 0 1-1.988-2.951 9.034 9.034 0 0 1-.732-3.622 9.05 9.05 0 0 1 .733-3.626 9.394 9.394 0 0 1 1.99-2.954 9.406 9.406 0 0 1 2.951-1.988 9.034 9.034 0 0 1 3.622-.732 9.05 9.05 0 0 1 3.626.733 9.394 9.394 0 0 1 2.954 1.99 9.406 9.406 0 0 1 1.988 2.951 9.034 9.034 0 0 1 .732 3.622 9.05 9.05 0 0 1-.733 3.626 9.394 9.394 0 0 1-1.99 2.954 9.405 9.405 0 0 1-2.951 1.988 9.033 9.033 0 0 1-3.622.732ZM12 19.9c2.198 0 4.064-.767 5.598-2.3 1.534-1.534 2.301-3.4 2.301-5.599 0-2.198-.767-4.064-2.3-5.598C16.064 4.868 14.198 4.1 12 4.1c-2.198 0-4.064.767-5.598 2.3C4.868 7.936 4.1 9.802 4.1 12c0 2.198.767 4.064 2.3 5.598C7.936 19.132 9.802 19.9 12 19.9Z"></path>
               \n
            </svg>
            \n\x3C!--?--> 
         </i>
         \x3C!--?lit$192891070$-->3/94 security vendors flagged this domain as malicious 
      </div>
      \x3C!--?lit$192891070$--> 
      <div class="hstack gap-4 fw-semibold ms-auto">
         \x3C!--?lit$192891070$--> 
         <a role="button" class="hstack gap-1">
            <i class="hstack fs-5">
               \x3C!--?lit$192891070$-->\x3C!--?lit$192891070$-->
               <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24" fill="currentColor">
                  \n  
                  <g clip-path="url(#a)">
                     \n    
                     <path d="M5.038 18.616a8.256 8.256 0 0 0 2.817 1.871 8.606 8.606 0 0 0 3.193.62 8.606 8.606 0 0 0 3.193-.62 8.256 8.256 0 0 0 2.817-1.87l-1.06-1.062c-1.379 1.38-3.029 2.069-4.95 2.069-1.92 0-3.57-.69-4.95-2.069-1.378-1.378-2.068-3.028-2.068-4.95 0-1.92.69-3.57 2.068-4.949 1.38-1.379 3.03-2.068 4.95-2.068 1.921 0 3.571.69 4.95 2.068l.188.188h-2.247l-.022 1.512 4.848-.007-.007-4.861-1.512.021v2.274l-.188-.188a8.256 8.256 0 0 0-2.817-1.87 8.607 8.607 0 0 0-3.193-.62 8.607 8.607 0 0 0-3.193.62 8.256 8.256 0 0 0-2.817 1.87 8.255 8.255 0 0 0-1.871 2.818 8.606 8.606 0 0 0-.62 3.193c0 1.084.206 2.148.62 3.193a8.256 8.256 0 0 0 1.87 2.817Z"></path>
                     \n  
                  </g>
                  \n  
                  <defs>
                     \n    
                     <clipPath id="a">
                        \n      
                        <path d="M0 0h24v24H0z"></path>
                        \n    
                     </clipPath>
                     \n  
                  </defs>
                  \n
               </svg>
               \n\x3C!--?-->
            </i>
            Reanalyze 
         </a>
         <a id="vtiAction" role="button" class="hstack gap-1" hidden="">
            <i class="hstack fs-5">
               \x3C!--?lit$192891070$-->\x3C!--?lit$192891070$-->
               <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24" fill="currentColor">
                  \n  
                  <path d="m19.441 20.403-6.197-6.2a5.386 5.386 0 0 1-1.707.955 5.993 5.993 0 0 1-1.981.336c-1.674 0-3.09-.578-4.245-1.734-1.155-1.156-1.733-2.568-1.733-4.237 0-1.67.577-3.083 1.731-4.24 1.155-1.158 2.567-1.737 4.238-1.737 1.67 0 3.085.579 4.242 1.736 1.158 1.157 1.737 2.57 1.737 4.241a5.88 5.88 0 0 1-.352 2.02 5.616 5.616 0 0 1-.94 1.681l6.2 6.186-.993.993Zm-9.89-6.308c1.281 0 2.364-.442 3.248-1.325.885-.884 1.328-1.967 1.328-3.25s-.443-2.366-1.328-3.25c-.884-.883-1.968-1.325-3.25-1.325-1.281 0-2.364.442-3.247 1.326-.883.883-1.325 1.967-1.325 3.25s.442 2.366 1.325 3.25c.884.882 1.967 1.324 3.25 1.324Z"></path>
                  \n
               </svg>
               \n\x3C!--?-->
            </i>
            Search 
         </a>
         <vt-ui-menu id="main" class="position-relative">
            <slot name="trigger" slot="trigger">
               <button type="button" class="btn btn-link p-0 dropdown-toggle fw-semibold hstack gap-1" aria-disabled="false">
                  <i class="hstack fs-5">
                     \x3C!--?lit$192891070$-->\x3C!--?lit$192891070$-->
                     <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24" fill="currentColor">
                        \n  
                        <path fill-rule="evenodd" d="M15.5 6.75c-1.722 0-3.082.625-4.287 1.179l-.032.015C9.942 8.513 8.865 9 7.52 9c-.8 0-1.354-.086-1.81-.215-.463-.13-.85-.313-1.343-.55l-.005-.002a7.041 7.041 0 0 1-.293-.152l-.04-.021a14.283 14.283 0 0 0-.33-.173 4.027 4.027 0 0 0-.415-.185 1.58 1.58 0 0 0-.535-.108v1.5c-.021 0-.035-.002-.039-.002a.556.556 0 0 1 .058.018c.065.024.15.063.257.117.094.047.19.098.294.154l.042.022c.113.061.239.128.357.184.486.234.981.471 1.584.642.61.173 1.305.271 2.218.271 1.69 0 3.034-.618 4.23-1.167l.056-.027C13.042 8.74 14.132 8.25 15.5 8.25c1.344 0 2.24.356 3.037.736l.318.155c.687.34 1.472.727 2.395.727v-1.5c-.549 0-.989-.214-1.696-.557l-.372-.18c-.9-.428-2.026-.881-3.682-.881Zm-.5 6.5c-1.739 0-2.983.637-4.074 1.195l-.024.012c-1.104.566-2.051 1.043-3.381 1.043-.8 0-1.354-.085-1.81-.215-.463-.13-.85-.313-1.343-.55l-.005-.002a6.995 6.995 0 0 1-.293-.152l-.04-.021c-.102-.055-.216-.117-.33-.173a4.027 4.027 0 0 0-.415-.185 1.581 1.581 0 0 0-.535-.108v1.5c-.021 0-.035-.002-.039-.002a.644.644 0 0 1 .058.018c.065.024.15.063.257.117.094.047.19.098.295.154l.04.022c.114.061.24.128.358.184.486.234.981.471 1.584.642.61.173 1.305.271 2.218.271 1.706 0 2.936-.63 4.019-1.184l.046-.023c1.1-.564 2.06-1.043 3.414-1.043 1.409 0 2.437.363 3.358.75l.386.165c.33.144.671.29.993.406.466.167.967.297 1.513.297v-1.5c-.307 0-.626-.072-1.007-.209a13.53 13.53 0 0 1-.854-.35l-.449-.191c-1.001-.422-2.244-.868-3.94-.868Z" clip-rule="evenodd"></path>
                        \n
                     </svg>
                     \n\x3C!--?-->
                  </i>
                  Similar 
               </button>
            </slot>
            <vt-ui-submenu class="dropdown-menu show" name="tools" id="submenu" role="menu" style="position: absolute; inset: 0px auto auto 0px; margin: 0px; transform: translate3d(0px, 26.4px, 0px);" data-popper-placement="bottom-start"> \x3C!--?lit$192891070$--> <a id="graph" role="button" target="_blank" class="hstack gap-2 dropdown-item" data-submenu-close-on-click="" href="https://www.virustotal.com/gui/search/entity%253Adomain%2520fuzzy_domain%253Awww.iuhjn.pplink.club"> Similar by domain name </a> </vt-ui-submenu>
         </vt-ui-menu>
         <a id="graph" role="button" class="hstack gap-1">
            <i class="hstack fs-5">
               \x3C!--?lit$192891070$-->\x3C!--?lit$192891070$-->
               <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24" fill="currentColor">
                  \n  
                  <path fill-rule="evenodd" d="M3 3h5.187v1.945l.47-.005.015 1.5-.485.005v.86l.439.439-1.06 1.06-.638-.637h-.563v.49h-1.5v-.49H3V3Zm1.5 1.5v2.167h2.187V4.5H4.5ZM15.818 3h5.187v5.167h-1.703v.49h-1.5v-.49h-.725l-.637.637-1.06-1.06.438-.44v-.933l-.455.005-.015-1.5.47-.005V3Zm1.5 1.5v2.167h2.187V4.5h-2.187ZM11 10h2c.04 0 .078.002.116.007l1.096-1.096 1.06 1.06L14 11.245V13c0 .038-.002.075-.006.111l.86.86-1.061 1.06L12.76 14h-1.517l-1.032 1.031-1.06-1.06.855-.855A1.032 1.032 0 0 1 10 13v-1.761L8.733 9.972l1.06-1.06 1.096 1.094c.036-.004.073-.006.111-.006Zm3.96 6.199.858.857v.753l-.344.003.014 1.5.33-.003v1.694h5.187v-5.168h-1.703v-.487h-1.5v.487h-1.084l-.697-.697-1.06 1.06Zm2.358 1.136v2.168h2.187v-2.168h-2.187Zm-13.568-1.5H3v5.168h5.187v-1.62l.61-.007-.014-1.5-.596.006v-.825l.858-.858-1.06-1.06-.698.697h-.922v-.488h-1.5v.487H3.75Zm.75 3.668v-2.168h2.187v2.168H4.5Zm.365-6.385v-2.23h1.5v2.23h-1.5Zm8.253-8.22-2.23.02.014 1.5 2.23-.02-.014-1.5Zm4.684 8.22v-2.23h1.5v2.23h-1.5Zm-4.559 4.716-2.23.021.015 1.5 2.23-.021-.014-1.5Z" clip-rule="evenodd"></path>
                  \n
               </svg>
               \n\x3C!--?-->
            </i>
            Graph 
         </a>
         <a href="https://docs.virustotal.com/reference/domain-info" target="_blank" class="hstack gap-1">
            <i class="hstack fs-5">
               \x3C!--?lit$192891070$-->\x3C!--?lit$192891070$-->
               <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24" fill="currentColor">
                  \n  
                  <path fill-rule="evenodd" d="M15.869 4.85h-1.5v4.326h-2.64v1.5h2.64v2.26h-2.64v1.5h2.64v4.583h1.5v-2.193l1.015.003a2.75 2.75 0 0 0 2.758-2.75v-1.426h2.107v-1.5h-2.107V9.716a2.75 2.75 0 0 0-2.743-2.75l-1.03-.003V4.85Zm-5.637.03v14.17h-1.5v-2.115l-1.04-.002a2.75 2.75 0 0 1-2.742-2.75v-1.437h-2.1v-1.5h2.1V9.819a2.75 2.75 0 0 1 2.757-2.75l1.025.003V4.881h1.5ZM6.45 9.82a1.25 1.25 0 0 1 1.253-1.25l1.02.002v6.863l-1.027-.002a1.25 1.25 0 0 1-1.246-1.25V9.819Zm9.428-1.357v6.863l1.01.003a1.25 1.25 0 0 0 1.254-1.25V9.716a1.25 1.25 0 0 0-1.247-1.25l-1.017-.003Z" clip-rule="evenodd"></path>
                  \n
               </svg>
               \n\x3C!--?-->
            </i>
            API 
         </a>
      </div>
   </div>
   <div class="card-body d-flex">
      \x3C!--?lit$192891070$--> 
      <div class="vstack gap-2 my-auto">
         <div class="hstack gap-4">
            <div class="vstack gap-2 align-self-center text-truncate me-auto">
               <div class="text-truncate">
                  \x3C!--?lit$192891070$-->www.iuhjn.pplink.club 
                  <vt-ui-punycode punycode="www.iuhjn.pplink.club"></vt-ui-punycode>
               </div>
               <div class="text-truncate"> <a href="https://www.virustotal.com/gui/domain/pplink.club"> \x3C!--?lit$192891070$-->pplink.club </a> </div>
            </div>
            \x3C!--?lit$192891070$--> 
            <div class="vr my-3"></div>
            <div>
               <div class="text-body-tertiary">Registrar</div>
               <a> \x3C!--?lit$192891070$-->GoDaddy.com, LLC </a> 
            </div>
            \x3C!--?lit$192891070$--> 
            <div class="vr my-3"></div>
            <div>
               <div class="text-body-tertiary">Creation Date</div>
               <a>
                  <vt-ui-time-ago unixtime="1653976937" data-tooltip-text="2022-05-31 06:02:17 UTC"></vt-ui-time-ago>
               </a>
            </div>
            \x3C!--?lit$192891070$--> 
            <div class="vr my-3"></div>
            <div>
               <div class="text-body-tertiary">Last Analysis Date</div>
               <vt-ui-time-ago unixtime="1722641728" data-tooltip-text="2024-08-02 23:35:28 UTC"></vt-ui-time-ago>
            </div>
            \x3C!--?lit$192891070$-->
            <div class="vr my-3"></div>
            \x3C!--?lit$192891070$--> 
            <div class="report-card-img-size rounded-circle hstack img-thumbnail">
               \x3C!--?lit$192891070$-->\x3C!--?lit$192891070$-->
               <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24" fill="currentColor">
                  \n  
                  <path d="M8.378 20.564a9.01 9.01 0 0 0 3.622.734v-1.399c-2.24-.022-4.116-.802-5.63-2.341C4.858 16.018 4.1 14.166 4.1 12c0-.296.022-.592.063-.887.042-.296.088-.594.138-.893l4.76 4.76h.963V12H8.04v-1.979h1.979a.97.97 0 0 0 .713-.288.97.97 0 0 0 .288-.715V7.061h1.96c.546 0 1.013-.194 1.4-.582.386-.387.58-.853.58-1.397v-.42a7.68 7.68 0 0 1 3.167 2.34 7.837 7.837 0 0 1 1.622 3.554h1.429c-.34-2.236-1.371-4.105-3.094-5.604-1.723-1.5-3.75-2.25-6.08-2.25a9.047 9.047 0 0 0-3.627.733 9.373 9.373 0 0 0-2.952 1.991 9.461 9.461 0 0 0-1.99 2.952 9.007 9.007 0 0 0-.733 3.62c0 1.286.244 2.494.733 3.625a9.372 9.372 0 0 0 1.991 2.952 9.463 9.463 0 0 0 2.952 1.99Z"></path>
                  \n  
                  <path d="m13.098 16.295 1.472 1.472.87-.87-1.47-1.471a1.677 1.677 0 0 1-.513-1.23c0-.477.17-.886.511-1.228.341-.34.75-.511 1.229-.51.478 0 .887.17 1.229.511l1.47 1.472.87-.87-1.471-1.473a2.864 2.864 0 0 0-2.097-.872 2.854 2.854 0 0 0-2.098.87 2.864 2.864 0 0 0-.872 2.1c0 .819.29 1.518.87 2.099Z"></path>
                  \n  
                  <path d="m16.04 14.245-.795.795 3.134 3.134.795-.795-3.134-3.135Z"></path>
                  \n  
                  <path d="m16.522 17.978-.87.87 1.472 1.473c.58.58 1.28.87 2.097.872a2.854 2.854 0 0 0 2.097-.87 2.864 2.864 0 0 0 .873-2.1c0-.819-.29-1.518-.87-2.099l-1.473-1.472-.87.87 1.471 1.471c.342.342.512.751.513 1.23 0 .477-.17.886-.512 1.227-.34.341-.75.512-1.228.512s-.887-.171-1.229-.513l-1.47-1.47Z"></path>
                  \n
               </svg>
               \n\x3C!--?--> 
            </div>
            \x3C!--?lit$192891070$--> 
         </div>
         \x3C!--?lit$192891070$--> 
      </div>
   </div>
</div>
"""

d = {}

soup = BeautifulSoup(f, "html.parser")

positives = soup.find("div", {"class": "hstack gap-2 fw-bold text-danger"}).text

url = soup.find("div", {"class": "vstack gap-2 align-self-center text-truncate me-auto"}).find("div", {"class": "text-truncate"}).text

details_div = soup.find("div", {"class": "hstack gap-4"}).find_all("div", recursive=False)

exists_registrar = details_div[2].find("div", {"class": "text-body-tertiary"}).text


if exists_registrar == "Registrar":
    d['registrar'] = details_div[2].find("a").text.replace("\n", "").strip()
else:
    d['registrar'] = "Unknown"


d['positives'] = positives.replace("\n", "").strip()
d['url'] = url.replace("\n", "").strip()

print(d)