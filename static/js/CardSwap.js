// CardSwap Component - Vanilla JavaScript with GSAP
class CardSwap {
  constructor(container, options = {}) {
    this.container = document.querySelector(container);
    if (!this.container) {
      console.error('Container not found:', container);
      return;
    }

    // Configuration
    this.width = options.width || 500;
    this.height = options.height || 400;
    this.cardDistance = options.cardDistance || 60;
    this.verticalDistance = options.verticalDistance || 75;
    this.delay = options.delay || 5000;
    this.pauseOnHover = options.pauseOnHover !== false;
    this.skewAmount = options.skewAmount || 6;
    this.easing = options.easing || 'elastic';

    // Easing configuration
    this.config =
      this.easing === 'elastic'
        ? {
            ease: 'elastic.out(0.7,0.8)',
            durDrop: 0.8,
            durMove: 0.8,
            durReturn: 0.8,
            promoteOverlap: 0.85,
            returnDelay: 0.1
          }
        : {
            ease: 'power1.inOut',
            durDrop: 0.6,
            durMove: 0.6,
            durReturn: 0.6,
            promoteOverlap: 0.4,
            returnDelay: 0.15
          };

    this.refs = [];
    this.order = [];
    this.tlRef = null;
    this.intervalRef = null;

    this.init();
  }

  makeSlot(i, distX, distY, total) {
    return {
      x: i * distX,
      y: -i * distY,
      z: -i * distX * 1.5,
      zIndex: total - i
    };
  }

  placeNow(el, slot, skew) {
    gsap.set(el, {
      x: slot.x,
      y: slot.y,
      z: slot.z,
      xPercent: -50,
      yPercent: -50,
      skewY: skew,
      transformOrigin: 'center center',
      zIndex: slot.zIndex,
      force3D: true
    });
  }

  init() {
    // Get all cards from container
    this.refs = Array.from(this.container.querySelectorAll('.card'));
    const total = this.refs.length;

    // Initialize order
    this.order = Array.from({ length: total }, (_, i) => i);

    // Set container dimensions
    this.container.style.width = this.width + 'px';
    this.container.style.height = this.height + 'px';

    // Place cards
    this.refs.forEach((el, i) => {
      this.placeNow(el, this.makeSlot(i, this.cardDistance, this.verticalDistance, total), this.skewAmount);
    });

    this.startSwapping();

    if (this.pauseOnHover) {
      this.addHoverEvents();
    }
  }

  swap = () => {
    if (this.order.length < 2) return;

    const [front, ...rest] = this.order;
    const elFront = this.refs[front];
    const tl = gsap.timeline();
    this.tlRef = tl;

    tl.to(elFront, {
      y: '+=500',
      duration: this.config.durDrop,
      ease: this.config.ease
    });

    tl.addLabel('promote', `-=${this.config.durDrop * this.config.promoteOverlap}`);
    rest.forEach((idx, i) => {
      const el = this.refs[idx];
      const slot = this.makeSlot(i, this.cardDistance, this.verticalDistance, this.refs.length);
      tl.set(el, { zIndex: slot.zIndex }, 'promote');
      tl.to(
        el,
        {
          x: slot.x,
          y: slot.y,
          z: slot.z,
          duration: this.config.durMove,
          ease: this.config.ease
        },
        `promote+=${i * 0.15}`
      );
    });

    const backSlot = this.makeSlot(this.refs.length - 1, this.cardDistance, this.verticalDistance, this.refs.length);
    tl.addLabel('return', `promote+=${this.config.durMove * this.config.returnDelay}`);
    tl.call(
      () => {
        gsap.set(elFront, { zIndex: backSlot.zIndex });
      },
      undefined,
      'return'
    );
    tl.to(
      elFront,
      {
        x: backSlot.x,
        y: backSlot.y,
        z: backSlot.z,
        duration: this.config.durReturn,
        ease: this.config.ease
      },
      'return'
    );

    tl.call(() => {
      this.order = [...rest, front];
    });
  };

  startSwapping() {
    this.swap();
    this.intervalRef = window.setInterval(this.swap, this.delay);
  }

  addHoverEvents() {
    const node = this.container;
    const pause = () => {
      this.tlRef?.pause();
      clearInterval(this.intervalRef);
    };
    const resume = () => {
      this.tlRef?.play();
      this.intervalRef = window.setInterval(this.swap, this.delay);
    };

    node.addEventListener('mouseenter', pause);
    node.addEventListener('mouseleave', resume);
  }

  destroy() {
    if (this.intervalRef) {
      clearInterval(this.intervalRef);
    }
    if (this.tlRef) {
      this.tlRef.kill();
    }
  }
}
