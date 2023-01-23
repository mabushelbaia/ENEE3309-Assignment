t = (0:0.00000001:0.1)';
a0 = 0.75;
a = [-0.20264, 0, -0.02252];
b = [0.31831, 0.15915, 0.10610];
T0 = 0.1;
g = heaviside(t) - 20 * (t - T0 / 2) .* heaviside(t - T0 / 2) + 20 * (t -
T0) .* heaviside(t - T0); ↪→
approx = a0;

for n = 1:3
    approx = approx + a(n) * cos(2 * pi * n * t / T0) + b(n) * sin(2 * pi * n * t / T0);
end

plot(t, approx, t, g)
xlabel('t')
ylabel('g(t)')
legend('ga(t)', 'g(t)')
axis([0 0.1 0 2])
