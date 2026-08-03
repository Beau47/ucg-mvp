function celebrateXP(amount) {

    // Create XP popup

    const popup = document.createElement("div");

    popup.className = "xp-popup";

    popup.textContent = `+${amount} XP 🎉`;

    document.body.appendChild(popup);


    // Confetti burst

    confetti({

        particleCount: 150,

        spread: 90,

        origin: {
            y: 0.6
        }

    });


    // Additional side bursts

    setTimeout(() => {

        confetti({

            particleCount: 80,

            angle: 60,

            spread: 70,

            origin: {
                x: 0
            }

        });


        confetti({

            particleCount: 80,

            angle: 120,

            spread: 70,

            origin: {
                x: 1
            }

        });

    }, 200);


    // Remove popup after animation

    setTimeout(() => {

        popup.remove();

    }, 2300);

}
