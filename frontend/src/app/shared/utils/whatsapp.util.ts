/** Monta um link `wa.me` a partir de um número (com ou sem formatação) e uma mensagem opcional. */
export function linkWhatsApp(numero: string, mensagem?: string): string {
  const numeroLimpo = numero.replace(/\D/g, '');
  const base = `https://wa.me/${numeroLimpo}`;
  return mensagem ? `${base}?text=${encodeURIComponent(mensagem)}` : base;
}
