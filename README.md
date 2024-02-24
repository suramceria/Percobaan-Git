Disposition untuk setiap kasus pada GrabFood

DAX minta cancel karena PAX


```mermaid
flowchart TD;
    A([Mulai])-->B[DAX minta dicancelkan agent];
    B-->C{PoP ada?};
    C-->D{ingin mengubah data?};
    D--Ya-->E[update nama/jumlah/harga: update_item];
    E-->TI(( ));
    D--Tidak-->TI;
    TI-->F{ingin membatalkan item?};
    F--Ya-->G[hapus item: delete_item, ulangi transaksi: reset_transaction];
    G-->U(( ));
    F--Tidak-->U;
    U-->H{ingin menambah item?};
    H--Ya-->C;
    H--Tidak-->I[mengecek dan menampilkan pesanan: check_order];
    I-->J{input sudah benar?};
    J--Ya, pemesanan sudah benar-->K[menghitung total belanja: total_price];
    J--Tidak, terdapat kesalahan input data-->E;
    K-->L{total belanja<200.000?};
    L--Ya-->M[tidak mendapatkan diskon];
    M-->V(( ));
    L--Tidak-->N{total belanja>200.000>=300.000?};
    N--Ya-->O[diskon 5%];
    O-->V;
    N--Tidak-->P{total belanja>300.000>=500.000?};
    P--Ya-->Q[diskon 8%]
    Q-->V;
    P--Tidak-->T{total belanja >500.000};
    T--Ya-->Z[diskon 10%];
    Z-->V;
    V-->R[menampilkan total belanja setelah diskon];
    R-->S([Selesai]);
