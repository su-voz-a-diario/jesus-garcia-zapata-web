
document.addEventListener('DOMContentLoaded', () => {
    const siteHeader = document.querySelector('.site-header');
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const mainNav = document.querySelector('.main-nav');

    if (siteHeader) {
        let isTicking = false;

        const updateHeaderState = () => {
            siteHeader.classList.toggle('is-scrolled', window.scrollY > 8);
            isTicking = false;
        };

        window.addEventListener('scroll', () => {
            if (isTicking) return;

            isTicking = true;
            window.requestAnimationFrame(updateHeaderState);
        }, { passive: true });

        updateHeaderState();
    }
    
    if (mobileMenuBtn && mainNav) {
        const icon = mobileMenuBtn.querySelector('i');
        const desktopQuery = window.matchMedia('(min-width: 1181px)');

        const setMenuState = (isOpen) => {
            mainNav.classList.toggle('active', isOpen);
            mobileMenuBtn.setAttribute('aria-expanded', String(isOpen));

            if (!icon) return;
            icon.classList.toggle('fa-bars', !isOpen);
            icon.classList.toggle('fa-xmark', isOpen);
        };

        mobileMenuBtn.addEventListener('click', () => {
            setMenuState(!mainNav.classList.contains('active'));
        });

        mainNav.addEventListener('click', (event) => {
            if (event.target.closest('a')) {
                setMenuState(false);
            }
        });

        document.addEventListener('keydown', (event) => {
            if (event.key === 'Escape') {
                setMenuState(false);
                mobileMenuBtn.focus();
            }
        });

        document.addEventListener('click', (event) => {
            if (!mainNav.classList.contains('active')) return;
            if (mainNav.contains(event.target) || mobileMenuBtn.contains(event.target)) return;

            setMenuState(false);
        });

        desktopQuery.addEventListener('change', (event) => {
            if (event.matches) {
                setMenuState(false);
            }
        });

        setMenuState(false);
    }
});
