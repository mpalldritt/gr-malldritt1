% Reads erros from a file and sums them

f = fopen('BER-test-data.dat', 'rb');
values = fread(f, Inf, 'float');
total_errors = sum(values(:,1))
num_syms = size(values(:,1));
num_syms = num_syms(1)
ber = total_errors/num_syms
